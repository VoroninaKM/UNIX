#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
print('Соединение с сервером прошло успешно!')

while True:
    mas = input()
    if mas == 'exit':
        break
    sock.send(mas.encode())
    print('Данные отправлены серверу.')
    data = sock.recv(1024)
    print('Прием данных прошел успешно.')
    print(data.decode())

sock.close()
print('Разрыв соединения с сервером.')
