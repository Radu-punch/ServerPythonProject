from unittest import IsolatedAsyncioTestCase , main,mock
from Server.server import *
from Server.views import *
import socket
class ServerTest(IsolatedAsyncioTestCase):
    async def test_checkport_default(self):
             res = await check_port(33)
             self.assertEqual(res , 16666)

    async def test_checkport_usual(self):
            res =  await check_port(4444)
            self.assertEqual(res,4444)

    async def test_give_header(self):
            ras='HTTP/1.1 200 OK'.encode()+'\r\n'.encode()+'Content-Type: text/html; charset=utf-8'.encode()+'\r\n\r\n'.encode()
            res = await give_header('200','html')
            self.assertEqual(res,ras)

    async def test_give_header_code_404(self):
            ras='HTTP/1.1 404 Not Found'.encode()+'\r\n'.encode()+'Content-Type: text/css'.encode()+'\r\n\r\n'.encode()
            res=await give_header('404','css')
            self.assertEqual(res,ras)

    async def test_request_parser(self):
            req='GET /favicon.ico HTTP/1.1'.encode()
            res = await request_parser(req)
            self.assertEqual(res,('GET','/favicon.ico','ico'))
    async def test_server_responce_501(self):
            req='HTTP/1.1 501 Not Implemented\r\nContent-Type: text/html; charset=utf-8'.encode()+'\r\n\r\n'.encode()+'''
                <html>
                      <head><title>501 NOT IMPLEMENTED</title></head>
                      <body><h1>501 NOT IMPLEMENTED</h1></body>
                </html>
                 '''.encode()
            rasp= await server_response('OPTIONS /favicon.ico HTTP/1.1'.encode())
            self.assertEqual(rasp,req)
    async def test_server_responce_404(self):
            ras='HTTP/1.1 404 Not Found'.encode()+'\r\n'.encode()+'Content-Type: text/html; charset=utf-8'.encode()\
                +'\r\n\r\n'.encode()+'''
                <html>
                    <head><title>404 PAGE NOT FOUND</title></head>
                    <body><h1>404 PAGE NOT FOUND</h1></body>
                </html>
                        '''.encode()

            req =  await error_404()
            self.assertEqual(req,ras)

    async def test_exception_server_responce(self):
        with mock.patch('server.server_response', side_effect=FileNotFoundError, create=True):
            rasp = await server_response('GET /aaaa.html HTTP/1.1'.encode())
            req = ras='HTTP/1.1 404 Not Found'.encode()+'\r\n'.encode()+'Content-Type: text/html; charset=utf-8'.encode()\
                +'\r\n\r\n'.encode()+'''
                <html>
                    <head><title>404 PAGE NOT FOUND</title></head>
                    <body><h1>404 PAGE NOT FOUND</h1></body>
                </html>
                        '''.encode()
        self.assertEqual(rasp, req)

    async def test_mentenance(self):
            ras='HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode()\
              +'''<!doctype html>\r\n<html>\r\n<head>\r\n    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">\r\n    <title>PythonWebServer</title>\r\n</head>\r\n<body>\r\n<h1>This site is under maintenance</h1>\r\n<p>Please come back later</p>\r\n</body>\r\n</html>'''.encode()
            req=await MentinanceReDirect()
            self.assertEqual(req,ras)
    async def test_server_responce_200(self):
        with mock.patch('server.server_response',  create=True):
            rasp = await server_response('GET /LinkedFile.html HTTP/1.1'.encode())
            req = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode()+'''<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>Abobus</title>\r\n</head>\r\n<body>\r\n<h1>second page</h1>\r\n        <p>caz de test pentru serverul meu</p>\r\n\r\n</body>\r\n</html>'''.encode()
        self.assertEqual(rasp,req)
    async def test_conect_server(self):
        sok = await conect_to_socket(16000)
        self.assertTrue(sok, True)


if __name__ == '__main__':
    main()
