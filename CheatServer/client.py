import socket

def connect_to_server():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port number
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Receive data from the server
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {data}")
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    connect_to_server()