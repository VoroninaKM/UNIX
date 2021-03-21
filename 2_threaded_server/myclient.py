#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('192.168.1.45', 9090))
print('Соединение с сервером прошло успешно!')

sock.send('Hello, world!'.encode())
print('Данные отправлены серверу.')

data = sock.recv(1024)
print('Прием данных прошел успешно.')
print(data.decode())
sock.close()
print('Разрыв соединения с сервером.')