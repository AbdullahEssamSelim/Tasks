import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send a message to the server
message = "A" * 1024 * 1024  # Sending a large message of 1MB
client_socket.sendall(message.encode())

# Close the connection
client_socket.close()
