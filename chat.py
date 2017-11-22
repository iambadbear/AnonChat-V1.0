import socket
import time
import threading
from threading import Thread

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port=8080

count=0

print("Connecting...")
while count==0:
    try:
        s.connet(("localhost",port))
        count +=1
        
    except:
            pass
           
        
print("Succesfully connected !!")


def listen():
    
    global s

    while True:
        data =s.recv(1024)
        print ("localhost>")+str(data)


def Send():
    
    global s

    while True:

        msg = raw_input(">")
        s.send(msg)


       
if __name__=="__main__":
    Thread(target=listen).start()
    Thread(target=Send).start()

