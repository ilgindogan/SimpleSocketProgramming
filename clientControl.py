import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "10.3.0.26"              # Ip address that the TCPServer  is there
port = 8888                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send('Hello server!'.encode())

with open('received_file', 'wb') as f:
    while True:
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
s.close()
print('connection closed')
