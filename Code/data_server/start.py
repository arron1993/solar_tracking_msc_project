from server.server import Server

from threading import Thread


def main():
    data_server = Server()
    start_thread = Thread(target=data_server.start_server)
    start_thread.start()

    request_thread = Thread(target=data_server.request_measurements)
    request_thread.start()


if __name__ == '__main__':
    main()
