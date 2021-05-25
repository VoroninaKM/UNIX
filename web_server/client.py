import socket

sock = socket.socket()
sock.connect(('localhost', 8081))
sock.send("Подключение успешно".encode())

data = sock.recv(1024)
sock.close()

print(data.decode())
