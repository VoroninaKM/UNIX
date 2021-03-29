import socket
import threading


def recv_data(sock):
    while True:
        data = sock.recv(1024)
        print('\r' + data.decode() + '\n' + 'Вы: ', end='')



host = '127.0.0.1'
port = int(input('Введите порт: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((host, port))

if not port:
    port = 9000
else:
    port = int(port)


while True:
    nick = input('Введите имя: ')
    nickname = '<nick_check>='+nick
    if nick == 'exit':
        sock.close()
        print('Отключение')
        break

    sock.send(nickname.encode())
    data = sock.recv(1024)
    data = data.decode()
    if data == '<nick_check_true>':
        print(f'Вы вошли в чат!, {nick}')
        break
    elif data == '<nick_check_false>':
        print(f'Выберите имя')


tread = threading.Thread(target=recv_data, args=(sock,), daemon=True)
tread.start()
sock.send('enter'.encode())

while True:
    data = input(f'вы: ')
    sock.send(data.encode())
    if data == 'exit':
        sock.close()
        print('Отключение')
        break