import socket

from thread import ServerThread


def handler(request: str) -> str:
    print(request)

    meta, content = request.split("\r\n\r\n", 2)
    first_line, *headers = meta.split("\r\n")
    method, resource, *_ = first_line.split(" ")
    with open("files" + resource) as f:
        content = f.read()

        return f"""HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: {len(content)}

{content}
"""


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen(5)


def close():
    server_socket.close()


try:
    while True:
        (client_socket, address) = server_socket.accept()
        ct = ServerThread(client_socket, handler)
        ct.run()
except KeyboardInterrupt:
    server_socket.close()
