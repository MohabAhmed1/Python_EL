import socket
import random
import threading



s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
ip = socket.gethostbyname(socket.gethostname())
def server_thread(client,address):
    try:
        rodata = client.recv(1024)
        msg = f' "id":"XYZ" , "Value" = {random.randint(100, 500)} ,"type" : "Temperature "'
        msg_encoded = msg.encode('UTF-8')
        print(msg)
        print(address)
        client.send(msg_encoded)
    except ConnectionResetError:
        print(f"Connection lost with {client_address}")    
    finally:    
        client.close()

s.bind((ip,5000))
s.listen(5)
while(True):
    client,address = s.accept()
    serv = threading.Thread(target=server_thread, args=(client, address))
    serv.start()
    