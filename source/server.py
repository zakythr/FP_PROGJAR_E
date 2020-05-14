import socket
import select
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '127.0.0.1'
port = 8081
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []

def operation(val1, op, val2):
    print(op)
    if(op == "+"):
        return val1 + val2
    elif(op == "*"):
        return val1 * val2
    elif(op == "-"):
        return val1 - val2
    elif(op == "/"):
        return val1 / val2
    
flag = "0"
step = "0"
namefile = ""
path = "D:/kuliah/semester 6/PROGJAR/sourcecode/server/"

def clientthread(conn, addr):
    global flag
    global step
    while True:
        try:
            message = conn.recv(2024).decode()
            if message:
                if (flag == "0"):
                    flag = message
                elif (flag == "1"):
                    if (step == "0"):
                        step = "1"
                        namefile = message.rstrip()
                    else:
                        step = "0"
                        flag = "0"
                        message_to_send = '<' + addr[0] + '>' + 'mengirim ' + namefile
                        print(message_to_send)
                        broadcast(message_to_send, conn)
                        with open(path+namefile, "w") as f:
                            f.write(message)
                elif (flag == "2"):
                    flag = "0"
                    s = message
                    c = ""
                    val = ""
                    result = 0
                    for i in range(len(s)):
                        if(s[i] == "+"):
                            if(c==""):
                                c = s[i]
                                result = int(val)
                                val = ""
                            else:
                                result = operation(result, c, int(val))
                                c = s[i]
                                val = ""
                        elif(s[i] == "*"):
                            if(c==""):
                                c = s[i]
                                result = int(val)
                                val = ""
                            else:
                                result = operation(result, c, int(val))
                                c = s[i]
                                val = ""
                        elif(s[i] == "-"):
                            if(c==""):
                                c = s[i]
                                result = int(val)
                                val = ""
                            else:
                                result = operation(result, c, int(val))
                                c = s[i]
                                val = ""
                        elif(s[i] == "/"):
                            if(c==""):
                                c = s[i]
                                result = int(val)
                                val = ""
                            else:
                                result = operation(result, c, int(val))
                                c = s[i]
                                val = ""
                        else:
                            val += s[i]
                    message_to_send = '<' + addr[0] + '>' + s.rstrip() + "=" + str(operation(result, c, int(val)))
                    print('<' + addr[0] + '>' + s)
                    broadcast(message_to_send, conn)
                elif (flag == "3"):
                    flag = "0"
                    print('<' + addr[0] + '>' + message.rstrip())
                    message_to_send = '<' + addr[0] + '>' + message.rstrip()
                    broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue
        
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)
                
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + 'connected')
    threading.Thread(target=clientthread, args=(conn,addr)).start()
    
conn.close()