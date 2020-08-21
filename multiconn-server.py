import socket

host = '127.0.0.1'
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()
print('Connected by client 1', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()