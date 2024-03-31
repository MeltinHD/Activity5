# Activity5

This activity combines concurrency and socket programming to create a concurrent echo server in Python. 
The server is capable of handling multiple client connections at the same time, echoing back messages sent from the clients.

Server.py:
- The server starts by creating a socket and binding it to localhost and chosen port.
- The server listens for any incoming client connections.
- The server loops to accept multiple client connections.
- Each client connection is targeted to a new thread
- Inside the thread, it loops to receive multiple messages from the client, prints message, and echos back to client, until the client types 'quit'.
- Once client quits, the connections is closed for that client, and thread exits.

Client.py:
- The client creates a socket and connects to the server
- A blank message is created
- The client loops that prompts user for messages to send to the server.
- The messages are sent to the server and displays a response from the server.
- If user enters 'quit', send it to the server, close the socket and exit the application.
