import socket
import sys
class ipython_socket:
    def __init__(self, remote_ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((remote_ip, port))
            print "connected"
        except:
            print "could not connect"

    def sendrecv(self, message):
        """Send a message then read the response until a new line is
        received"""
        self.s.sendall(message);
        self.s.sendall("\n");

        while True:
            #TODO: this is not how this should be done
            recv_data = self.s.recv(1024)
            print(recv_data)
            if "\n" in recv_data:
                break

    def close(self):
        self.s.close()
