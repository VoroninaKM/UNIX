import socket
import pickle

def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [x - k for x in map(ord, c)]))

def check(m):
    sp = [1, 2, 3, 8]
    if int(m) in sp:
        return True
    else:
        print('Ключ некорректен')
        conn.send(pickle.dumps('exit'))
        conn.close()
        return False

sock = socket.socket()
sock.bind(('127.0.0.1', 8081))
sock.listen(1)
conn, addr = sock.accept()

file = open("keyS.txt", 'w')

p, g, b = 3, 2, 5
B = g ** b % p

# запись ключа в файл
file.write(str(B))
file.close()
keyB = open("keyS.txt").read()

if check(keyB):
    # отправлем открытый ключ сервера клиенту
    conn.send(pickle.dumps((p, g, int(keyB))))
    # получаем открытый ключ клиента
    msgK = conn.recv(1024)
    K = pickle.loads(msgK)[2] ** b % p
    # расшифровать сообщение клиента
    msgR = conn.recv(1024)
    msgR = decrypt(b, pickle.loads(msgR))
    msgR = decrypt(K, msgR)
    print("Message =", msgR)
    # отправить сообщение
    msg = encrypt(b, 'Hello, client!')
    msg = encrypt(K, msg)
    conn.send(pickle.dumps(msg))
    print("Send =", msg)

    conn.close()
