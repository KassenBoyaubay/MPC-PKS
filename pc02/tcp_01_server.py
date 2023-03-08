import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        try:
            # Print the new TCP connection to the console
            print("[{}]: open".format(self.client_address[0]))
            
            while True:
                data = self.request.recv(1024)
                if not data:
                    break
                print("[{}]: RX: {}".format(self.client_address[0], data))
                self.request.sendall(data.upper()+b'|')
                
        except Exception as e:
            print("[{}]: ER: {}".format(self.client_address[0], e))
            
        print("[{}]: disconnected".format(self.client_address[0]))


if __name__ == "__main__":
    HOST, PORT = "", 50000

    # Create the server
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

