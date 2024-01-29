
import socket

class Remote:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_ip = None
        self.client_port = None
        self.client_addr = None

    def connect(self, host, port):
        self.client_ip = host
        self.client_port = port
        self.client_addr = (host, port)

        try:
            print(f"[+] connecting to {host} in port {port}")
            self.client_socket.connect(self.client_addr)
            print(f"[+] Connected")

        except ConnectionRefusedError:
             print(f"[+] Connection refused")
             exit()

        socket_killed = False

        while not socket_killed:
            command = input(f"[{self.client_ip}]/~: ")

            if "kill server" in command:
                self.client_socket.close()
                break

            self.client_socket.sendall(command.encode())

            output = self.client_socket.recv(1024).decode()
            print(output)

if __name__ == "__main__":
    remote = Remote()
    host = "127.0.0.1"
    port = 1234
    remote.connect(host, port)

