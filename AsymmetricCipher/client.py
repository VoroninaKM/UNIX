import socket
import pickle

def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [x - k for x in map(ord, c)]))

sock = socket.socket()
sock.connect(('127.0.0.1', 8081))

file = open("keyC.txt", 'w')

p, g, a = 3, 2, 5
A = g ** a % p

# запись ключа в файл
file.write(str(A))
file.close()
keyA = open("keyC.txt").read()

# отправляем открытый ключ клиента серверу
sock.send(pickle.dumps((p, g, int(keyA))))  
# получаем открытый ключ сервера
msgK = sock.recv(1024)
K = pickle.loads(msgK)[2] ** int(a) % p
# отправить сообщение серверу 
msg = encrypt(a, 'Hello!')
msg = encrypt(K, msg)
sock.send(pickle.dumps(msg))
print("Send =", msg)
# сообщение сервера
msgR = sock.recv(1024)
msgR = decrypt(a, pickle.loads(msgR))
msgR = decrypt(K, msgR)
print("Message serv=" , msgR)

sock.close()
