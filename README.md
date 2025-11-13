
# 📌 **README.md**

# Python Socket Client–Server (Echo + File Transfer) using Docker

This project demonstrates a simple **TCP Client–Server model** using Python sockets.
It includes:

* Echo server
* File transfer (client → server)
* Dockerized environment
* Docker Compose for multi-container setup

---

## 🚀 Features

### **1. Echo Function**

Client sends a string → Server returns the uppercase version.

### **2. File Upload**

Client sends a file (`sample.txt`) →
Server receives it and saves it as `recv.txt`.

### **3. Docker Support**

Both client and server run in separate Docker containers.

---

## 📁 Project Structure

```
socket_demo/
│-- server.py
│-- client.py
│-- sample.txt
│-- recv.txt
│-- Dockerfile
│-- docker-compose.yml
│-- README.md
```

---

## 🖥️ Server Code (server.py)

```python
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
```

---

## 🖥️ Client Code (client.py)

```python
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
```

---

## 🐳 Docker Setup

### **Dockerfile**

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . /app
```

### **docker-compose.yml**

```yaml
services:
  server:
    build: .
    command: python server.py
    volumes:
      - .:/app
    working_dir: /app

  client:
    build: .
    command: python client.py
    depends_on:
      - server
    volumes:
      - .:/app
    working_dir: /app
```

---

## ▶️ How to Run

Run this command in your project folder:

```
docker compose up --build
```

### **Expected Output**

```
HELLO
File saved
```

---

## ✔ Output Explanation

* First output = Echo from server
* Second output = Server confirmed file upload
* Uploaded file saved as `recv.txt`

---

## 📌 Author

**Aditi (aditikp0907)**
GitHub: [https://github.com/aditikp0907](https://github.com/aditikp0907)

---


