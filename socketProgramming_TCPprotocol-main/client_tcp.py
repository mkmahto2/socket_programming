import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_IP=input("Enter Server IP: ")
server_port=int(input("Enter server port: "))
s.connect((server_IP,server_port))
while True:
    send_msg=input("What msg you want send on the server {}: ".format(server_IP))
    if(send_msg=='exit'):
        s.send(b"exit")
        s.close()
        break
    send_msg=send_msg.encode()
    s.send(send_msg)
    reply_server=s.recv(1024)
    reply_server=reply_server.decode()
    print("msg received from the server"+": "+reply_server)
