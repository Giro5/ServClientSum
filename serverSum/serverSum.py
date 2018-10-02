import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
print("Сервер запущен")
while True:
    conn, addr = sock.accept()
    print ('connected:', addr)
    while True:
        data = conn.recv(1024).decode("utf-8")
        if not data:
            print("losted:", addr)
            break
        a = []
        for i in range(len(data)-5):
            for j in range(i+5, len(data)):
                a.append(int(data[i])+int(data[j]))
        print("Value:", data)
        print("All sums:", a)
        print("Max:", max(a))
        conn.send(str(max(a)).encode("utf-8"))
    if input()=='exit':
            sock.close()
            break

