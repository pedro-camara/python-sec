import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket created")

host = "localhost"
port = 5432
s.bind((host, port))
mensage = "Server: Hello World!"

while 1:
    data, addr = s.recvfrom(4096)
    if not data:
        break
    print("Client: " + data.decode())
    s.sendto(mensage.encode(), addr)
    