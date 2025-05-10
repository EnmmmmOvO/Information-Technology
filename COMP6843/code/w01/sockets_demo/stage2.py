import socket

from thread import ServerThread


def handler(request: str) -> str:
    print(request)

    method, resource, *_ = request.split(" ")
    try:
        with open("files" + resource) as f:
            return f"""200 OK
{f.read()}
"""
    except (IsADirectoryError, FileNotFoundError):
        return """404 Not Found
Not found.
"""


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8080))
server_socket.listen(5)


try:
    while True:
        (client_socket, address) = server_socket.accept()
        ct = ServerThread(client_socket, handler)
        ct.run()
except KeyboardInterrupt:
    server_socket.close()
