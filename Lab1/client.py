import socket

from Lab1.config import encoding, address

post = """POST /auth HTTP/1.1\r\nContent-Type: text/html; charset=utf-8\r\n\r\nuserName=Ganesh&password=pass"""
get = """GET /home HTTP/1.1\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"""

command_line_args = {
    ("h", "help"): [],
    ("g", "generic"): [],
    "Host": [],
    "Content-Type": [],
    "Connection": [],
    "charset=utf-8": [],
    "Cache-Control": [],
    "sec-ch-ua": [],
    "sec-ch-ua-mobile": [],
    "sec-ch-ua-platform": [],
    "Upgrade-Insecure-Requests": [],
    "User-Agent": [],
    "Accept": [],
    "Sec-Fetch-Site": [],
    "Sec-Fetch-Mode": [],
    "Sec-Fetch-User": [],
    "Sec-Fetch-Dest": [],
    "Accept-Encoding": [],
    "Accept-Language": [],
    "Cookie": []
}


def main(argument):
    print(f"Argument: {argument}")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)
    content = f"{get}".encode(encoding)
    client.send(content)
    print(client.recv(1024).decode(encoding))


if __name__ == '__main__':
    # sys.argv[1]
    main(1)
