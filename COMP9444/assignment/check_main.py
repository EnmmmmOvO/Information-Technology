"""
   check_main.py
   COMP9444, CSE, UNSW
"""

import torch
import torch.utils.data
import torch.nn.functional as F
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
from check import MLP


def train(net, train_loader, optimizer):
    total = 0
    correct = 0
    for batch_id, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()  # zero the gradients
        output = net(data)  # apply network
        loss = F.binary_cross_entropy(output, target)
        loss.backward()  # compute gradients
        optimizer.step()  # update weights
        pred = (output >= 0.5).float()
        correct += (pred == target).float().sum()
        total += target.size()[0]
        accuracy = 100 * correct / total
    if epoch % 100 == 0:
        print('ep:%5d loss: %6.4f acc: %5.2f' %
              (epoch, loss.item(), accuracy))
    return accuracy


def test(net):
    with torch.no_grad():  # suppress updating of gradients
        net.eval()  # toggle batch norm, dropout
        correct = 0
        total = 0
        for batch_id, (data, target) in enumerate(train_loader):
            output = net(data)  # apply network
            loss = F.binary_cross_entropy(output, target)
            pred = (output >= 0.5).float()
            correct += (pred == target).float().sum()
            total += target.size()[0]
            accuracy = 100 * correct / total
        net.train()  # toggle batch norm, dropout back again
        return accuracy.item();


def graph_hidden(net, node):
    xrange = torch.arange(start=-1.5, end=1.5, step=0.01, dtype=torch.float32)
    yrange = torch.arange(start=-1.5, end=1.5, step=0.01, dtype=torch.float32)

    xcoord = xrange.repeat(yrange.size()[0])
    ycoord = torch.repeat_interleave(yrange, xrange.size()[0], dim=0)
    grid = torch.cat((xcoord.unsqueeze(1), ycoord.unsqueeze(1)), 1)

    with torch.no_grad():  # suppress updating of gradients
        net.eval()  # toggle batch norm, dropout
        output = net(grid)
        net.train()
        hid = (net.hid >= 0.5).float()
        # plot function computed by model
        plt.clf()
        plt.pcolormesh(xrange, yrange, (hid.cpu()[:, node]).view(yrange.size()[0], xrange.size()[0]), cmap='Wistia',
                       shading='auto')


def graph_output(net):
    xrange = torch.arange(start=-1.5, end=1.5, step=0.01, dtype=torch.float32)
    yrange = torch.arange(start=-1.5, end=1.5, step=0.01, dtype=torch.float32)
    xcoord = xrange.repeat(yrange.size()[0])
    ycoord = torch.repeat_interleave(yrange, xrange.size()[0], dim=0)
    grid = torch.cat((xcoord.unsqueeze(1), ycoord.unsqueeze(1)), 1)

    with torch.no_grad():  # suppress updating of gradients
        net.eval()  # toggle batch norm, dropout
        output = net(grid)
        net.train()  # toggle batch norm, dropout back again
        pred = (output >= 0.5).float()
        # plot function computed by model
        plt.clf()
        plt.pcolormesh(xrange, yrange, pred.cpu().view(yrange.size()[0], xrange.size()[0]), cmap='Wistia')


# command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--hid', type=int, default='4', help='number of hidden units')
parser.add_argument('--act', type=str, default='sig', help='sig or step')
parser.add_argument('--init', type=float, default=0.15, help='initial weight size')
parser.add_argument('--set_weights', default=False, action='store_true')
parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
parser.add_argument('--epoch', type=int, default='200000', help='max training epochs')
args = parser.parse_args()

df = pd.read_csv('check.csv')

data = torch.tensor(df.values, dtype=torch.float32)

num_input = data.shape[1] - 1

full_input = data[:, 0:num_input]
full_target = data[:, num_input:num_input + 1]

# print(full_input)

train_dataset = torch.utils.data.TensorDataset(full_input, full_target)
train_loader = torch.utils.data.DataLoader(train_dataset,
                                           batch_size=train_dataset.__len__())

# choose network architecture
net = MLP(args.hid, args.act)

if list(net.parameters()):
    # initialize weight values
    if args.set_weights:
        net.set_weights()
    else:
        for m in list(net.parameters()):
            m.data.normal_(0, args.init)

    # delete this
    graph_output(net)
    plt.scatter(full_input[:, 0], full_input[:, 1],
                c=full_target[:, 0], cmap='brg_r', vmin=-2, vmax=1)
    plt.savefig('./plot/check.jpg', format='jpg')

    # use Adam optimizer
    optimizer = torch.optim.Adam(net.parameters(), lr=args.lr,
                                 weight_decay=0.00001)
    #optimizer = torch.optim.SGD(net.parameters(),lr=args.lr,momentum=0.9,
    #                                 weight_decay=0.00001)

    accuracy = 0
    if args.set_weights:
        print('Initial Weights:')
        for m in list(net.parameters()):
            print(m.data)
        accuracy = test(net)
        print('Initial Accuracy: ', accuracy)

    # training loop
    if args.act == 'sig' and accuracy < 100.0:
        epoch = 0
        count = 0
        while epoch < args.epoch and count < 2000:
            epoch = epoch + 1
            accuracy = train(net, train_loader, optimizer)
            if accuracy == 100:
                count = count + 1
            else:
                count = 0
        print('Final Weights:')
        for m in list(net.parameters()):
            print(m.data)
        accuracy = test(net)
        print('Final Accuracy: ', accuracy)

    # graph hidden units
    if args.hid <= 30:
        for node in range(args.hid):
            graph_hidden(net, node)
            plt.scatter(full_input[:, 0], full_input[:, 1],
                        c=full_target[:, 0], cmap='brg_r', vmin=-2, vmax=1)
            plt.savefig('./plot/hid_%d_%d.jpg' \
                        % (args.hid, node))

    # graph output unit
    graph_output(net)
    plt.scatter(full_input[:, 0], full_input[:, 1],
                c=full_target[:, 0], cmap='brg_r', vmin=-2, vmax=1)
    plt.savefig('./plot/out_%d.jpg' % args.hid, format='jpg')
