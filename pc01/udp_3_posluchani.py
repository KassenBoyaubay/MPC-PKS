import socket
import struct
import time

#adresa a port prijemce (zada vyucujici)
dst_host = "147.229.150.101"
dst_port = 50000

#vytvoreni socketu
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Rn1 = 71
for i in range(5):
    seq = i    
    n1 = 71
    n2 = Rn1

    #seq, n1 a n2 jsou prenasena cisla
    msg = struct.pack("!LLL", seq, n1, n2)
    
    #zaslani zpravy
    n = udp_socket.sendto(msg, (dst_host, dst_port))
    print("Odeslano {} byte\n".format(n))
    
    try:
        msg_rcv, address = udp_socket.recvfrom(512)
        Rseq, Rn1, Rn2 = struct.unpack("!LLL", msg_rcv)
    except TimeoutError:
        print("No response from server")
    except struct.error:
        print("Unable to unpack packet from {}".format(address))
    else:
        lg = "a={}, p={}, s={}, n1={}, n2 ={}".format(*address, Rseq, Rn1, Rn2)
        print(lg)
    
    time.sleep(0.5)

#uzavreni socketu
udp_socket.close()  