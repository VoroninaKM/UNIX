import socket
import threading

class T(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self, name="t" + n)
        self.n = n

    def run(self):
        print("Процесс", self.n)

    def go(self,conn):
        data = conn.recv(1024)
        if not data:
            conn.send(("Сообщения нет").encode())  
        else:
            conn.send(data.upper())

sock = socket.socket()
sock.bind(('', 9091))

while True:
    lst = [] 
    sock.listen(3)
    conn, addr = sock.accept()
    lst.append(conn)
    print(lst)
    for i in range(len(lst)):
        j=T(f"{i}")
        j.start()
        j.go(lst[i])
        conn.close()