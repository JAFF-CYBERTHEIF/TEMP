import socket

# Set up the network socket
HOST = "27.62.59.201"  # Replace with your Raspberry Pi IP address
PORT = 8089

print("connecting....")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("connected")

while True:

    # Send data to the server
    message = int(input("Enter angle 0 - 180 : "))
    
    if message == None:
        continue
    else:
        print("msg ",message)
        s.send(message.encode("utf-8"))

# Close the network connection and destroy the window
s.close()
