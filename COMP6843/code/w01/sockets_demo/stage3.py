import socket

from thread import ServerThread


def handler(request: str) -> str:
    print(request)

    first_line, *headers = request.split("\r\n")
    method, resource, *_ = first_line.split(" ")
    try:
        with open("files" + resource) as f:
            content = f.read()
        return f"""HTTP/1.1 200 OK
Content-Type: image/png
Content-Length: {len(content)}

{content}
"""
    except (IsADirectoryError, FileNotFoundError):
        content = "Not found."
        return f"""HTTP/1.1 404 Not Found
Content-Type: text/plain
Content-Length: {len(content)}

{content}
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
