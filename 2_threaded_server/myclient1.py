import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9091))
print('Соединение с сервером прошло успешно!')

sock.send('Hello, world!'.encode())
print('Данные отправлены серверу.')

data = sock.recv(1024)
print('Прием данных прошел успешно.')
print(data.decode())
sock.close()
print('Разрыв соединения с сервером.')