import socket

soc = socket.socket()

soc.bind(('', 9090))
soc.listen(1)

conn, addr = soc.accept()

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(data)

conn.close()

