import socket
from threading import Thread
from typing import Callable


class ServerThread(Thread):
    def __init__(self, client_socket: socket.socket, handler: Callable[[str], str]):
        super().__init__()
        self.socket = client_socket
        self.handler = handler

    def kill(self):
        if self.socket:
            self.socket.close()
            self.socket = None

    def run(self):
        while self.socket:
            buffer = b""

            try:
                new_data = self.socket.recv(8192)
            except socket.timeout:
                print("timeout")
                continue
            except socket.error:
                print("error")
                self.kill()
                break

            if len(new_data) == 0:
                self.kill()
                break

            buffer += new_data

            self.socket.sendall(self.handler(buffer.decode()).encode())
            self.kill()
