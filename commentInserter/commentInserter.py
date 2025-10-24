import socket

# Set up a TCP server to receive comments
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind(("0.0.0.0", 7777))
server.bind(("localhost", 7777))
server.listen(1)

client, add = server.accept()

comments = client.recv(65536)

# Split the received comments into a list
comments = list(comments.decode().splitlines())
print(comments)

# Read the original Python file
with open("demo.py", "r") as file:
    data = file.readlines()

# Insert comments before each function definition
output = []
for line in data:
    if line.strip().startswith("def "):
        output.append(comments.pop(0) + "\n")
    output.append(line)

print(output)

# Write the modified code with comments to a new file
with open("demoCommented.py", "w") as finalOutput:
    finalOutput.writelines(output)