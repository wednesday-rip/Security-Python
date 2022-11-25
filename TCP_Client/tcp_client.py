import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("Connection Failed")   
        print(f"Error {error}")
        sys.exit()
    print("Socket created successfully")
    print("-" * 60)
    
    host = input("Enter the host or IP to connect: ")
    port = input("Enter the port to connect: ")
    
    try:
        s.connect((host, int(port)))
        print(f"TCP client connected to host: {host} on port: {port}")
        s.shutdown(2) 
    
    except socket.error as e:
        print("Connection Failed")        
        print(f"Error {error}")
        sys.exit()
        
        
        
if __name__ == "__main__":
    main()        