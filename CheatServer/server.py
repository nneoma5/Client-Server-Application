import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port number
    
    # Bind the socket to the port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")
        
        # Send a message to the client
        message = "Hello, you are connected to the server!"
        client_socket.send(message.encode('utf-8'))
        
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()