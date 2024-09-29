import socket
import random
import threading
import time

ip = socket.gethostbyname(socket.gethostname())

def client_thread():
    while(True):
    
        global ip
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip,5000))
        msg = 'I got the message'
        msg_encoded = msg.encode('UTF-8')
        print(msg)
        client.send(msg_encoded)
        client.close()
        time.sleep(1)

client_thread = threading.Thread(target=client_thread)
client_thread.start()
