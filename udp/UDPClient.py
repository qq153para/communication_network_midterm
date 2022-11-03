import socket

msg_from_client = "Hello UDP Server"

server_address_port = ("192.168.0.11", 614)
buffer_size = 1024

UDP_client_socket = socket.socket(family= socket.AF_INET, type = socket.SOCK_DGRAM)
while(True):
    msg_from_client = "hello udp server"
    bytes_to_send = str.encode(msg_from_client)
    UDP_client_socket.sendto(bytes_to_send, server_address_port)
    msg_from_server = UDP_client_socket.recvfrom(buffer_size)
    msg = "Message from Server:{}".format(msg_from_server[0])
    print(msg)