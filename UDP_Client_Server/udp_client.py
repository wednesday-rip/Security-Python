import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket client successfully created")

host = "localhost"
port = 5433
msg = "Client: Text message to the server"

try:
    print(f"Client {msg}")
    s.sendto(msg.encode(), (host, port))
    
    data, server = s.recvfrom(4096)
    data = data.decode()
    print(f"Client: {data}")
    
finally:
    print("Client closing the connection")
    s.close()    