# _*_ coding: utf-8 _*_

import socket

host = '127.0.0.1'
port = 3434

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))

print('Connect %s:%d OK' % (host, port))
data = sock.recv(1024)
print("Received ", str(data, encoding='utf-8'))

sock.close()