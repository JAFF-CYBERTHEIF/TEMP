import socket

HOST = '0.0.0.0'  # Use '0.0.0.0' to listen on all available network interfaces
PORT = 1234  # Use any available port number (above 1024)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server listening on {HOST}:{PORT}')
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'Received data: {data.decode()}')
            conn.sendall(data)

            
            
            
            
            
import socket

SERVER_IP = '27.62.59.201'  # Replace with the public IP address of the server
SERVER_PORT = 1234  # Replace with the port number used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    print(f'Connected to server at {SERVER_IP}:{SERVER_PORT}')
    while True:
        message = input('Enter angle 0 - 180 : ')
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f'Received data: {data.decode()}')

