import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
import threading as th
ip="0.0.0.0"
port=1234
x=[]
s.bind((ip,port))
s.listen()
def myfun(c,addr):
    while True:
        c_recv=c.recv(1024)
        c_recv=c_recv.decode()
        print("msg received from the client {} : ".format(addr[0])+c_recv)
        if(c_recv=="exit"):
            break
        #reply=str(len(c_recv))
        reply=input("What msg you want to send to client {}: ".format(addr[0]))
        reply=reply.encode()
        c.send(reply)

def server():
    while True:
        c,addr=s.accept()
        myth=th.Thread(target=myfun,args=(c,addr))
        x.append(myth)
        myth.start()

server()
