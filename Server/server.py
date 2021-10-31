import socket
import threading
import re
http_status={
    '200': 'HTTP/1.1 200 OK',
    '400': 'HTTP/1.1 400 Bad Request',
    '404': 'HTTP/1.1 404 Not Found'
}
file_types={
    'html': 'Content-Type: text/html; charset=utf-8',
    'jpg': 'Content-Type: image/jpeg',
    'png': 'Content-Type: image/png',
    'css': 'Content-Type: text/css',
    'ico': 'Content-Type: image/x-icon'
}

def request_parser(request):
    buff=request.decode().split('\r\n')
    method, request, protocol = buff[0].split(' ')
    if request == '/': request = '/index.html'
    path = re.findall('[/a-z.]+', request)[0]
    file_type = path.split('.')[1]
    return method,path,file_type

def give_header(method,file_type):
    return http_status[method].encode() +'\r\n'\
           + file_types[file_type].encode() + '\r\n\r\n'


def server_response(request):
    method, path, file_type = request_parser(request)
    #if method=="GET":
    try:
        with open('views'+path,'rb') as file:
            data=file.read()
            header=give_header('200',file_type)
            return  header+data
    except FileNotFoundError:
            header=give_header('404',file_type)
            err_mes='''
        <html>
            <head><title>404 PAGE NOT FOUND</title></head>
            <body><h1>404 PAGE NOT FOUND</h1></body>
        </html>
        '''
            return header+err_mes



def MentinanceReDirect(url):
    response_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'+url
    return response_header
def StopServer(client):
    client.close()
def run():
    try:
        socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        socket_server.bind(('localhost',16666))
        socket_server.listen()

        while True:
            client , adresa = socket_server.accept()
            request = client.recv(4096)
            print(request.decode('utf-8'))
            print()
            print(adresa)
            response = server_response(request.decode('utf-8'))
            client.sendall(response)
            client.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        socket_server.close()

if __name__ == '__main__':
    run()