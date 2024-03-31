import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        # Create a blank message
        message = ""
        # Loops message input until user enters 'quit'
        while (True):
            if (message == 'quit'):
                break
            # Sends a message
            message = input("Enter Message (Type 'quit' to exit): ")
            s.sendall(message.encode())
            # Receive a response
            data = s.recv(1024)
            print(f'Received from server: {data.decode()}')

if __name__ == "__main__":
    start_client()
    