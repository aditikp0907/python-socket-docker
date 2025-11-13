import socket
s = socket.socket()
s.bind(('0.0.0.0', 5000))
s.listen(5)
while True:
    conn, _ = s.accept()
    data = conn.recv(1024)
    if data.startswith(b"FILE:"):
        with open("recv.txt", "wb") as f:
            f.write(data[5:])
        conn.send(b"File saved")
    else:
        conn.send(data.upper())
    conn.close()
