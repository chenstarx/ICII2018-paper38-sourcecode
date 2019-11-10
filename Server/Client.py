import socket
from time import time
host = "127.0.0.1"
port = 55880

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((host,port))

while True:

    message = input("Input: ")

    try:
        clientSocket.sendall(("Time: " + str(time()) + "; ").encode())
        receive = clientSocket.recv(1024).decode()
        print("recv: " + receive)

    except:
        clientSocket.close()

    print(receive, "\n")
