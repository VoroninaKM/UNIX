#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
print('Соединение с сервером прошло успешно!', file=open('log.txt','a'))

while True:
    mas = input()
    if mas == 'exit':
        break
    elif mas == 'cleaning log':
        with open('log.txt', 'w') as f:
            pass
    sock.send(mas.encode())
    print('Данные отправлены серверу.', file=open('log.txt','a'))
    data = sock.recv(1024)
    print('Прием данных прошел успешно.', file=open('log.txt','a'))
    print(data.decode())

sock.close()
print('Разрыв соединения с сервером.', file=open('log.txt','a'))

