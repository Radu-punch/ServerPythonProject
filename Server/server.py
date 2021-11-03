import socket
import threading
import re
import asyncio
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


async def request_parser(request):
        buff=request.decode().split('\r\n')
        method, request, protocol = buff[0].split(' ')
        if request == '/': request = '/index.html'
        path = re.findall('[/A-Za-z.]+', request)[0]
        file_type = path.split('.')[1]
        return method, path, file_type

async def give_header(code,file_type):
        return http_status[code].encode() +'\r\n'.encode()\
               + file_types[file_type].encode() + '\r\n\r\n'.encode()

async def check_port(port):
        default_port=16666
        if port>1024 and port<65000:
            return port
        else:
            return default_port

async def server_response(request):
            method, path, file_type = await request_parser(request)
            if method!="GET" and method!="HEAD":
                    res = await error_501()
                    return res
            else:
                try:
                    with open('views'+path,'rb') as file:
                        data=file.read()
                        header= await give_header('200',file_type)
                        return  header+data
                except FileNotFoundError:
                        res = await error_404()
                        return res

async def MentinanceReDirect():
    f=open('views/mentenanta.html', 'rb')
    data=f.read()
    response_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode()
    f.close()
    return response_header+data
async def error_404():
    header = await give_header('404', 'html')
    err_mes = '''
                <html>
                    <head><title>404 PAGE NOT FOUND</title></head>
                    <body><h1>404 PAGE NOT FOUND</h1></body>
                </html>
                        '''.encode()
    return header + err_mes
async def error_501():
    head = await give_header('501', 'html')
    err_m = '''
                <html>
                      <head><title>501 NOT IMPLEMENTED</title></head>
                      <body><h1>501 NOT IMPLEMENTED</h1></body>
                </html>
                 '''.encode()
    return head + err_m

async def StopServer(client):
    client.close()


async def run(port,stare):

        socket_server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        port1= await check_port(port)
        socket_server.bind(('localhost',port1))
        socket_server.listen()
        while True:
            client , adresa = socket_server.accept()
            request = client.recv(4096)
            print(request.decode('utf-8'))
            print()
            print(adresa)
            if stare==1:
                response = await server_response(request)
                client.sendall(response)
            elif stare == 3:
                ras = await MentinanceReDirect()
                client.sendall(ras)
                client.shutdown(socket.SHUT_WR)



if __name__ == '__main__':
    asyncio.run(run(4000,1))