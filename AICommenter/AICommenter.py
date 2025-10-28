import socket

# Set up a TCP server to receive parsed data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
#server.bind(("localhost", 9999))
server.listen(1)

client, add = server.accept()

parsedData = client.recv(65536)
parsedData = list(parsedData.decode().splitlines())
print(parsedData)

# comments = []
with open("comments.txt", 'w') as commentsFile:
    for lines in parsedData:
        if "functionName" in lines:
                commentsFile.writelines("# This is the function: " + lines[22:-1] + "\n")

# Send the generated comments to the commentInserter service using TCP socket connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("inserter", 7777))
#client.connect(("localhost", 7777))

file = open('comments.txt', 'r')

client.send(file.read().encode())

file.close()
client.close()