import socket
import threading
import sys

def handle_request(client, addr):
    data = client.recv(1024).decode()
    req = data.split("\r\n")
    method, path, _ = req[0].split(" ")

    if path == "/":
        response = "HTTP/1.1 200 OK\r\n\r\nhello".encode()
    elif path.startswith("/echo"):
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(path[6:])}\r\n\r\n{path[6:]}".encode()
    elif path.startswith("/user-agent"):
        user_agent = req[2].split(": ")[1]
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}".encode()
    elif path.startswith("/files"):
        directory = sys.argv[2]
        filename = path[7:]

        if method == "GET":
            try:
                with open(f"{directory}/{filename}", "r") as f:
                    body = f.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(body)}\r\n\r\n{body}".encode()
            except FileNotFoundError:
                response = f"HTTP/1.1 404 Not Found\r\n\r\n".encode()
        elif method == "POST":
            content_length = 0
            for header in req[1:]:
                if header.startswith("Content-Length"):
                    content_length = int(header.split(": ")[1])

            if content_length > 0:
                body = req[-1]  # Assuming the request body is the last line of the request
                with open(f"{directory}/{filename}", "w") as f:
                    f.write(body)
                response = "HTTP/1.1 201 Created\r\n\r\n".encode()
            else:
                response = "HTTP/1.1 400 Bad Request\r\n\r\n".encode()
        else:
            response = "HTTP/1.1 405 Method Not Allowed\r\n\r\n".encode()
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
    
    client.send(response)

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        client, addr = server_socket.accept()
        threading.Thread(target=handle_request, args=(client, addr)).start()

if __name__ == "__main__":
    main()