import socket
import sys

def main():
    try:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A connection error occurred: %s" % e)
        sys.exit(1)
        
    print("Socket created")
    
    hostTarget = input("Enter the host to connect to: ")
    portTarget = input("Enter the port to connect to: ")
    
    try:
        s.connect((hostTarget, int(portTarget)))
        print("Socket connected to %s on port %s" % (hostTarget, portTarget))
        s.shutdown(2)
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)