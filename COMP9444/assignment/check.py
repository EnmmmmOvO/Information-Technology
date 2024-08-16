"""
   check.py
   COMP9444, CSE, UNSW
"""

import torch
import torch.nn as nn
import matplotlib.pyplot as plt


class MLP(torch.nn.Module):
    def __init__(self, hid=4, act='sig'):
        super(MLP, self).__init__()
        # two hidden layers
        self.act = act
        self.in_hid = nn.Linear(2, hid)
        self.hid_out = nn.Linear(hid, 1)
        self.hid = None

    def forward(self, input):
        self.hid = torch.sigmoid(self.in_hid(input))
        if self.act == 'step':
            self.hid = (self.in_hid(input) >= 0).float()
            return (self.hid_out(self.hid) >= 0).float()
        else:  # sigmoid
            self.hid = torch.sigmoid(self.in_hid(input))
            return torch.sigmoid(self.hid_out(self.hid))

    def set_weights(self):
        # * Set weights and biases before scaling by 10 *
        # in_hid_weight = [[2, 2], [-2, 2], [2, -2], [-2, -2]]
        # hid_bias = [1, 1, 1, 1]
        # hid_out_weight = [[1, 1, 1, 1]]
        # out_bias = [-3]

        # Scale by 10
        in_hid_weight = [[20, 20], [-20, 20], [20, -20], [-20, -20]]
        hid_bias = [10, 10, 10, 10]
        hid_out_weight = [[10, 10, 10, 10]]
        out_bias = [-30]

        self.in_hid.weight.data = torch.tensor(
            in_hid_weight, dtype=torch.float32)
        self.in_hid.bias.data = torch.tensor(
            hid_bias, dtype=torch.float32)
        self.hid_out.weight.data = torch.tensor(
            hid_out_weight, dtype=torch.float32)
        self.hid_out.bias.data = torch.tensor(
            out_bias, dtype=torch.float32)
