from unittest import TestCase , main
from Server.WebServer.server import *

class ServerTest(TestCase):
    def test_checkport_default(self):
        self.assertEqual(check_port(33) , 16666)

    def test_checkport_usual(self):
        self.assertEqual(check_port(4444),4444)

    def test_give_header(self):
        ras='HTTP/1.1 200 OK'.encode()+'\r\n'.encode()+'Content-Type: text/html; charset=utf-8'.encode()+'\r\n\r\n'.encode()
        self.assertEqual(give_header('200','html'),ras)

    def test_give_header_code_404(self):
        ras='HTTP/1.1 404 Not Found'.encode()+'\r\n'.encode()+'Content-Type: text/css'.encode()+'\r\n\r\n'.encode()
        self.assertEqual(give_header('404','css'),ras)

    def test_request_parser(self):
        req='GET /favicon.ico HTTP/1.1'.encode()
        self.assertEqual(request_parser(req),('GET','/favicon.ico','ico'))



if __name__ == '__main__':
    main()
