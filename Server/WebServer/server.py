import socket
import threading
import re
http_status={
    '200': 'HTTP/1.1 200 OK',
    '400': 'HTTP/1.1 400 Bad Request',
    '404': 'HTTP/1.1 404 Not Found',
    '501': 'HTTP/1.1 501 Not Implemented'
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
    path = re.findall('[/A-Za-z.]+', request)[0]
    file_type = path.split('.')[1]
    return method,path,file_type

def give_header(code,file_type):
    return http_status[code].encode() +'\r\n'.encode()\
           + file_types[file_type].encode() + '\r\n\r\n'.encode()

def check_port(port):
    default_port=16666
    if port>1024 and port<65000:
        return port
    else:
        return default_port

def server_response(request):
    method, path, file_type = request_parser(request)
    if method!="GET" and method!="HEAD":
        head = give_header('501', 'html')
        err_m = '''
                    <html>
                        <head><title>501 NOT IMPLEMENTED</title></head>
                        <body><h1>501 NOT IMPLEMENTED</h1></body>
                    </html>
                    '''.encode()
        return head+err_m
    elif method=="GET":
        try:
            with open('views'+path,'rb') as file:
                data=file.read()
                header=give_header('200',file_type)
                return  header+data
        except FileNotFoundError:
                header=give_header('404','html')
                err_mes='''
            <html>
                <head><title>404 PAGE NOT FOUND</title></head>
                <body><h1>404 PAGE NOT FOUND</h1></body>
            </html>
            '''.encode()
                return header+err_mes


def MentinanceReDirect():
    f=open('../views/mentenanta.html', 'rb')
    data=f.read()
    response_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode()
    return response_header+data

def StopServer(client):
    client.close()

def run(port,stare):
    try:
        socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        port1=check_port(port)
        socket_server.bind(('localhost',port1))
        socket_server.listen()
        while True:
            client , adresa = socket_server.accept()
            request = client.recv(4096)
            print(request.decode('utf-8'))
            print()
            print(adresa)
            if stare==1:
                response = server_response(request)
                client.sendall(response)
            elif stare == 3:
                client.sendall(MentinanceReDirect())

              #  client.shutdown(socket.SHUT_WR)


    except stare == 2 :
        StopServer(client)

if __name__ == '__main__':
    run(4000,3)