import socket
import os
import threading

def handle_client(c, addr):
    print(addr,"connected")

    with c:
        request = c.recv(1024)

        # Parse HTTP headers
        headers = request.split(b"\r\n")
        file = headers[0].split()[1].decode()

        # Load file content
        if file == "/":
            file= "/index.html"

        try:
            with open(WEBROOT + file, "rb") as f:
                content = f.read()
            response = b"HTTP/1.0 200 OK\r\n\r\n " + content

        except FileNotFoundError:
            response = b"HTTP/1.0 404 NOT FOUND\r\n\r\nFile not found!"

        # Send HTTP response
        c.sendall(response)