import socket
import time
import threading
from threading import Thread

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port=8080

s.bind(("",port))
s.listen(5)

print ("Waiting for Clients...")

client,addr=s.accept()

print("Client"+str(addr[0])+"has Connected !")

def listen():
    global s
    global client,addr

    while True:
        
        data = client.recv(1024)
        print (str(addr[0])+(">")+str(data))


def Send():
    global s
    global client,addr

    while True:
        
        msg=raw_input(">")
        client.send(msg)  

    
if __name__=="__main__":
    Thread(target= listen).start()
    Thread(target=Send).start()
