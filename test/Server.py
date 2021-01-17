# _*_ coding: utf-8 _*_
import socket
import datetime

host = '0.0.0.0'
port = 3434

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(1)

while True:
    conn, addr = server.accept()

    print('Client %s connected!' % str(addr))

    dt = datetime.datetime.now()
    message = "Current time is " + str(dt)

    conn.send(bytes(message, 'utf-8'))
    print('Send:', message)
    conn.close()
