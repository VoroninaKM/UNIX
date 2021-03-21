import socket
from threading import Thread

for port in range(1,10):
    sock = socket.socket()
    try:
        print(port)
        sock.connect(('192.168.1.45', port))
        print("Порт", port, "открыт")
    except:
        continue
    finally:
        sock.close()