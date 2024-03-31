import socket
import threading

# New function for client messages
def client_handle(clientConn, clientAddr):
   print(f'Connected by {clientAddr}')
   # Loops message received from client until no data
   while True:
        #Receive data from the client
        data = clientConn.recv(1024)
        if not data:
            break
        #send data back as a response
        print(f'Message by {clientAddr}: {data.decode()}')
        clientConn.sendall(data)

def start_server(host='127.0.0.1', port=65432):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f'Server started, listening on {host}:{port}')
        s.listen()

        #Accept a connection
        while (True):    
            thread1 = ""
            conn, addr = s.accept()
            # Creates new thread and targets to client function with conn and addr as arguments
            thread1 = threading.Thread(target=client_handle, args=(conn, addr))
            thread1.start()

if __name__ == "__main__":
    start_server()