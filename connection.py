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
        print('[+] Connection Established With {} On Port {}'.format(self.client_address[0],self.client_address[1]))
        return (self.client_conn, self.client_address)

    def SendData (self, user_input):
        user_input = bytes(user_input, "utf-8")
        self.client_conn.send(user_input)

    def recieve_data (self):
        recieve_data = self.client_conn.recv(1024)
        self_data = recieve_data.decode('utf-8')
        return self_data
