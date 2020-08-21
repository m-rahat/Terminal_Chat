import socket

HOST = 'Mohammeds-MBP.cable.rcn.com'  #Standard loopback interface address (localhost)
PORT = 65432        #Port to listen on (non-orivileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)

print(socket.gethostname())

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()

                