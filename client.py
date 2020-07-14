import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server socket
sock.connect((socket.gethostname(), 1234))
