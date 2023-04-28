import socket

from Lab1.config import number_of_access_clients, encoding, address, HDRS200, HDRS404


def configurate_server():
    server = socket.create_server(address)
    server.listen(number_of_access_clients)
    try:
        while True:
            print("Listen....")
            client_soc, addr = server.accept()
            data = client_soc.recv(1024).decode(encoding)
            content = get_request_data(data)
            print(data)
            with open("log.txt", "w") as file:
                file.write(data)
            client_soc.send(content)
            client_soc.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Shut down....")


def get_request_data(request):
    path = request.split(" ")[1]
    try:
        with open(f"./files{path}", "rb") as file:
            response = file.read()
        return HDRS200.encode(encoding) + response
    except FileNotFoundError:
        return (HDRS404 + "404 | Page not found!").encode(encoding)


def main():
    with open("log.txt", "w") as file:
        pass
    configurate_server()


if __name__ == '__main__':
    main()
