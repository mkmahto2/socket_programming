import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Using IPv4 and UDP protocol

senderip = input("Enter your IP address: ")
senderport = int(input("Enter your port: "))

s.bind((senderip, senderport)) #socket Created

receiverip = input("Enter the IP of the receiver: ")
receiverport = int(input("Enter the port of the receiver: "))

def receiveMessages():# Function for receiving messages
    while(True):
        data = s.recvfrom(1024)
        print('\n\t\t\t\t\t\t\t\t\tReceived -> ' + data[0].decode())
        time.sleep(0.2)

def sendMessages():  # Function for sending messages
    while(True):
        message = input("Enter the message: ")
        s.sendto(message.encode(), (receiverip, receiverport))
        print('Your Message : ', message)
        time.sleep(0.1)


receive = threading.Thread(target=receiveMessages)
send = threading.Thread(target=sendMessages)
    
receive.start()
send.start()
