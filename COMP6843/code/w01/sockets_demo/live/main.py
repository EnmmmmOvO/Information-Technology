import socket

from thread import ServerThread


def handler(request: str) -> str:
    print(request)

    first_line, *headers = request.split("\r\n")
    method, resource, *_ = first_line.split(" ")

    if "?" in resource:
        path, query_string = resource.split("?", 1)
    else:
        path = resource
        query_string = ""

    if query_string:
        params = {}
        for param in query_string.split("&"):
            key, value = param.split("=", 1)
            params[key] = value
        print(params)

    try:
        with open("files" + resource.strip()) as f:
            content = f.read()
            return f"""HTTP/1.1 200 OK\r
Content-Type: text/html\r
Content-Length: {len(content)}\r
\r
{content}"""
    except (IsADirectoryError, FileNotFoundError):
        content = "Not found."
        return f"""HTTP/1.1 404 Not Found\r
Content-Type: text/plain\r
Content-Length: {len(content)}\r
\r
{content}"""


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen(5)


try:
    while True:
        (client_socket, address) = server_socket.accept()
        ct = ServerThread(client_socket, handler)
        ct.run()
except KeyboardInterrupt:
    server_socket.close()
