import socket

# while True:
#     client_socket, client_addr = server_socket.accept()
#     print(f"Client Address: {client_addr}")
#     request = parseRequest(client_socket.recv(1024))
#     print(request)
#     request.split('\n')





class Server:
    def __init__(self, host: str, port: int):
    # Socket setup
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host,port))
        server_socket.listen(5)
        print(f"Listening on {host}:{port}.")


    # def get():
    #     print()
    

    # def head():
    #     print()
    

    # def post():
    #     print()


    # def put():
    #     print()

    
    # def patch():
    #     print()

    
    # def delete():
    #     print()

    
    # def options():
    #     print()


if __name__ == '__main__':
    server = Server("0.0.0.0",3000)