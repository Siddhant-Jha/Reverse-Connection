import socket

SERVER_IP = "192.168.43.22"
SERVER_PORT = 8080

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (SERVER_IP, SERVER_PORT)
    sock.connect(address)

    msg_recvd = sock.recv(1024)

    print(msg_recvd.decode())

    sock.close()