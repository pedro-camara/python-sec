import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket created")

host = "localhost"
port = 5432
message = "Client: Hello World!"

try:
    print("Client: " + message)
    s.sendto(message.encode(), (host, port))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print("Server: " + data)
    
finally:
    print("Closing connection to the server")
    s.close()

