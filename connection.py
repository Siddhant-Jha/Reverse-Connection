import socket

class serverConnection:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def createConnection (self, ip = "", port = 8080):
        self.server_ip = ip
        self.server_port = port
        self.address = (self.server_ip, self.server_port)
        self.socket.bind(self.address)

    def Listen (self, backlog = 5):
        self.socket.listen(backlog)

    def AcceptConnection (self):
        self.client_conn, self.client_address = self.socket.accept()
        return (self.client_conn, self.client_address)