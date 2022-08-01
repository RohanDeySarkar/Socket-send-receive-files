import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
client.connect(('localhost', 1002))  # 127.0.0.1

# file = open('data/b.jpg', 'rb')
file = open('data/a.txt', 'rb')

image_data = file.read(3000000) 

while image_data:
    client.send(image_data)
    image_data = file.read(3000000)

file.close()
client.close()