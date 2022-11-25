import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket client successfully created")

host = "localhost"
port = 5432

s.bind((host, port))
msg = "Server: Text message to the client"

while 1:
    data, address = s.recvfrom(4096)
    if data:
        print("Server sending message")
        s.sendto(data + (msg.encode()), end)
        