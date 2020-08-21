import socket

HOST = 'Mohammeds-MBP.cable.rcn.com'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'Hello World')
data = s.recv(1024)
s.close()

print('Received', repr(data))