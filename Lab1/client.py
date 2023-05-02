import socket
import sys

from config import address, encoding

http_ver = "HTTP/1.1"

post = """POST /auth HTTP/1.1\r\nContent-Type: text/html; charset=utf-8\r\n\r\nuserName=Ganesh&password=pass"""
get = """GET /home HTTP/1.1\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"""

methods = [
    "GET",
    "POST",
    "OPTIONS"
]

options = {
    "-me": "",
    "-pa": "",
    "-he": "",
    "-bo": ""
}


def parse_options(args):
    print(*args, sep=' ')
    for key in options.keys():
        if key in args:
            options[args[args.index(key)]] = args[args.index(key) + 1]


def get_request() -> str:
    return f"{options['-me']} {options['-pa']} {http_ver}\r\n{options['-he']}\r\n\r\n{options['-bo']}"


def main(argument):
    parse_options(argument)
    request = get_request()
    # print(request)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)
    content = f"{request}".encode(encoding)
    client.send(content)
    print(client.recv(1024).decode(encoding))


if __name__ == '__main__':
    main(sys.argv[1:])
