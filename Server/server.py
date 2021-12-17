import socket
import threading
import re
import asyncio

http_status = {
    '200': 'HTTP/1.1 200 OK',
    '400': 'HTTP/1.1 400 Bad Request',
    '404': 'HTTP/1.1 404 Not Found',
    '501': 'HTTP/1.1 501 Not Implemented'
}
file_types = {'html': 'Content-Type: text/html; charset=utf-8', 'jpg': 'Content-Type: image/jpeg',
              'png': 'Content-Type: image/png', 'css': 'Content-Type: text/css', 'ico': 'Content-Type: image/x-icon'}


def request_parser(request):
    buff = request.decode().split('\r\n')
    method, request, protocol = buff[0].split(' ')
    if request == '/': request = '/index.html'
    path = re.findall('[/A-Za-z%0-9.]+', request)[0]
    file_type = path.split('.')

    return method, path, file_type[1]


def give_header(code, file_type):
    return http_status[code].encode() + '\r\n'.encode() \
           + file_types[file_type].encode() + '\r\n\r\n'.encode()


def check_port(port):
    default_port = 16666
    if port > 1024 and port < 65000:
        return port
    else:
        return default_port


def server_response(request):
    method, path, file_type = request_parser(request)
    if method != "GET" and method != "HEAD":
        res = error_501()
        return res
    else:
        try:
            with open('views' + path, 'rb') as file:
                data = file.read()
                header = give_header('200', file_type)
                return header + data
        except FileNotFoundError:
            res = error_404()
            return res


def MentinanceReDirect():
    f = open('views/mentenanta.html', 'rb')
    data = f.read()
    response_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode()
    f.close()
    return response_header + data


def error_404():
    header = give_header('404', 'html')
    err_mes = '''
                <html>
                    <head><title>404 PAGE NOT FOUND</title></head>
                    <body><h1>404 PAGE NOT FOUND</h1></body>
                </html>
                        '''.encode()
    return header + err_mes


def error_501():
    head = give_header('501', 'html')
    err_m = '''
                <html>
                      <head><title>501 NOT IMPLEMENTED</title></head>
                      <body><h1>501 NOT IMPLEMENTED</h1></body>
                </html>
                 '''.encode()
    return head + err_m


def conect_to_socket(port):
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost', port))
    socket_server.listen()
    return socket_server


def aleg_stare(stare, client, request):
    match stare:
        case 1:
            response = server_response(request)
            client.sendall(response)
        case 3:
            ras = MentinanceReDirect()
            client.sendall(ras)
            client.shutdown(socket.SHUT_WR)
        case 2:
            client.close()

def get_stare():
    stare = int(input("Da stare intre 1-3: "))
    return stare

def get_port():
    port = int(input("da un port intre 1024-65000"))
    return port

# def run():
#     stare = get_stare()
#     port = get_port()
#     port = check_port(port)
#     socket_server = conect_to_socket(port)
#     while True:
#         client, adresa = socket_server.accept()
#         request = client.recv(4096)
#         print(request.decode('utf-8'))
#         print()
#         print(adresa)
#         threading.Thread(target=aleg_stare, args=(stare, client, request)).run()


# if __name__ == '__main__':
#     run()