import socket

from Lab1.config import encoding, address

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

post = """POST /auth HTTP/1.1\r\nContent-Type: text/html; charset=utf-8\r\n\r\nuserName=Ganesh&password=pass"""
get = """GET /home HTTP/1.1\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"""

content = f"{get}".encode(encoding)
client.send(content)
print(client.recv(1024).decode(encoding))
