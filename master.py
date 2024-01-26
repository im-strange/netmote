
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_ip = "127.0.0.1"
client_port = 12345
client_addr = (client_ip, client_port)
client_socket.connect(client_addr)

socket_killed = False

while not socket_killed:
    command = input(f"{client_ip}/~: ")

    if "kill server" in command:
        client_socket.close()
        break

    client_socket.sendall(command.encode())

    output = client_socket.recv(1024).decode()
    print(output)

