import socket
# AF_INET = ipv4, AF_INET6 = ipv6

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 1234))

sock.listen(5)

while True:
    # Endpoint knows about other Endpoint
    clientsocket, address = sock.accept()
    print("Connection from {adress} has been established. ", address)
