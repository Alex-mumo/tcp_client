import socket

target_host = "127.0.0.1"
target_port = 8000

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ipv4 and tcp client parameters

#connectiong with the client
client.connect((target_host, target_port))

#send data over the network
client.send("GET  / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = recv(4096)
print(response)