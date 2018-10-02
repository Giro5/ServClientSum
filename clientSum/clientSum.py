import socket
import time
import random

sock = socket.socket()
while True:
    try:
        sock.connect(('localhost', 9090))
        print("connected to server")
        break
    except BaseException:
        print("ну бывает")
        time.sleep(2)

while True:
        s = str(random.randint(0,10000000000000000000000))
        print("Value:",s)
        sock.send(s.encode("utf-8"))
        data = sock.recv(1024)
        print("Max:",data.decode("utf-8"))
        if input()=='exit':
            sock.close()
            break