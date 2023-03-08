import socket
import time

#adresa a port prijemce (zada vyucujici)
host = "147.229.150.101"
port = 50000

#vytvoreni socketu
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#otevrit kanal
tcp_socket.connect((host, port))

for i in range(5):
    
    time.sleep(1)
    
    #zaslani dat (odpoved je ukladana do bufferu)
    msg = "data" + str(i)
    tcp_socket.sendall(msg.encode('ascii'))
    
    #time.sleep(1)
    
    #prijem
    data = tcp_socket.recv(1024)
    print(data)

#uzavreni kanalu
tcp_socket.close()