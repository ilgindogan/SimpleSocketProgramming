import socket                   # Import socket module
import json
try:
    port = 8888                     # Reserve a port for your service every new transfer wants a new port or you must wait.
    s = socket.socket()             # Create a socket object
    host = "10.3.0.26"              # Get local machine name
    s.bind((host, port))            # Bind to the port
    s.listen(5)                     # Now wait for client connection.

    print('Server listening....')

    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))
        conn.send('Thank you for connecting'.encode())
        conn.close()
except Exception as e:
    print(e)
