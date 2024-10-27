import socket
from typing import Callable
import threading

class Server:
    def __init__(self, host: str, port: int):
        # Socket setup
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = host
        self.port = port
        self.routes = {}

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server is listening on {self.host}:{self.port}.")

        while True:
            conn, addr = self.server_socket.accept()
            print(f"Connection received from {addr}")
            threading.Thread(target=self.handle_request, args=(conn,)).start()

    def handle_request(self, conn):
        request = conn.recv(1024).decode()
        path = request.split(' ')[1] if ' ' in request else '/'

        if path in self.routes:
            response = self.routes[path]()
            conn.sendall(f"HTTP/1.1 200 OK\n\n{response}".encode())
        else:
            conn.sendall(b"HTTP/1.1 404 Not Found\n\nPath not found")
        conn.close()
        
    def get(self, func, path: str = "/"):
        self.routes[path] = func  

# Define an example function
def someFunction():
    return "Hello from /test!"

if __name__ == '__main__':
    server = Server("0.0.0.0", 3000)
    server.get(someFunction, "/test")
    server.start()