import socket

def request_parser(request):
    buff=request.split(' ')
    req_met=buff[0]
    url=buff[1]
    return (req_met,url)

def server_response(request):
    req_met , url = request_parser(request)


def run():
    socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.bind(('localhost',16666))
    socket_server.listen()

    while True:
        client , adresa = socket_server.accept()
        request = client.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(adresa)
        response = server_response(request.decode('utf-8'))
        client.sendall('Merge Serverul'.encode())
        client.close()

if __name__ == '__main__':
    run()