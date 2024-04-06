import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print('Server listening on', (HOST, PORT))

# Accept a connection
conn, addr = server_socket.accept()
print('Connected by', addr)

# Receive and print data from the client
data = b''
while True:
    chunk = conn.recv(1024)
    if not chunk:
        break
    data += chunk

print('Received message:', data.decode())

# Close the connection
conn.close()
