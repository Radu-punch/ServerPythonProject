import socket


def run():
    socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.bind(('localhost',16666))
    socket_server.listen()


if __name__ == '__main__':
    run()