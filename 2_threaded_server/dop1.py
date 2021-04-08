import socket
from threading import Thread

for port in range(9090,9093):
    sock = socket.socket()
    try:
        print(port)
        sock.connect(('127.0.0.1', port))
        print("Порт", port, "открыт")
    except:
        continue
    finally:
        sock.close()