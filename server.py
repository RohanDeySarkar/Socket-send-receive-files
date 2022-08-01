import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind(('localhost', 1002))  # 127.0.0.1
server.listen()

client_socket, client_address = server.accept()

# file = open('server_image.jpg', "wb")
file = open("server_file.txt", "wb")
chunk = client_socket.recv(3000000)  # stream-based protocol

while chunk:
    file.write(chunk)
    chunk = client_socket.recv(3000000)

file.close()
client_socket.close()