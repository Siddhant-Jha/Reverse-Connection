import socket

SERVER_IP = "192.168.43.22"
SERVER_PORT = 8080

if __name__ == "__main__":
    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (SERVER_IP, SERVER_PORT)
    sock.bind(address)
    sock.listen(1)

    print("[+] Waiting For Incoming Connection: ",SERVER_PORT)

    client_sock, client_add = sock.accept()

    print("[+] Connection Established: ", client_add())

    msg = "Server This Side"

    client_sock.send(msg.encode())

    client_sock.close()

    sock.close()