import socket

# 1st connection: Echo
s1 = socket.create_connection(('server', 5000))
s1.send(b"hello")
print(s1.recv(1024).decode())
s1.close()

# 2nd connection: File transfer
s2 = socket.create_connection(('server', 5000))
with open("sample.txt", "rb") as f:
    s2.send(b"FILE:" + f.read())
print(s2.recv(1024).decode())
s2.close()
