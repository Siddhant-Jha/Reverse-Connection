import socket

class serverConnection:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def createConnection (self, ip = "", port = 8080):
        self.server_ip = ip
        self.server_port = port
        self.address = (self.server_ip, self.server_port)
        self.socket.bind(self.address)