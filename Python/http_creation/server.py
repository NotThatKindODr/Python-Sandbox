
import http.server
import socketserver

class myTCPHandler(socketserver.BaseRequestHandler):
    def handle(self): 
        self.data = self.request.recv(1024).strip() #handle has the attr request which lets us access the request
        #recv reads everything that was sent in one sendall() call
        #1024 is the number of bits for it to read each time 
        #.strip removes first and last characters
        print(self.data)
        self.request.sendall("ACK from TCP Server".encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST, PORT), myTCPHandler)

    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()