import socket
import select
import sys
import msvcrt

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8081
server.connect((ip_address, port))

while msvcrt.kbhit():
    msvcrt.getch()

while True:
    sockets_list = [server]
    read_socket, write_socket, error_socket = select.select(sockets_list, [], [], 1)
    
        
    for socks in read_socket + [sys.stdin]:
        if socks == server:
            message = socks.recv(2048).decode()
            print(message)
        else:
            if msvcrt.kbhit():
                message = sys.stdin.readline()
                server.send(message.encode())
                sys.stdout.write('<You>')
                sys.stdout.write(message)
                sys.stdout.flush()
            
server.close()