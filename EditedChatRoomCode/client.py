import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7000))

# Flag to keep track of connection status
connected = True

# Listening to Server and Sending Nickname
def receive():
    global connected
    while connected:
        try:
            # Receive Message From Server
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            connected = False
            client.close()
            break

# Sending Messages To Server
def write():
    global connected
    while connected:
        message = '{}: {}'.format(nickname, input(''))
        try:
            client.send(message.encode('ascii'))
        except:
            print("Error sending message. You may have been disconnected.")
            connected = False

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
