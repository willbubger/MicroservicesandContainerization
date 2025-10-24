from ollama import chat, ChatResponse
import socket

# Set up a TCP server to receive parsed data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind(("0.0.0.0", 9999))
server.bind(("localhost", 9999))
server.listen(1)

client, add = server.accept()

parsedData = client.recv(65536)
print(parsedData)

# Use the Ollama API to generate comments for the parsed data
response: ChatResponse = chat(model='gemma3:1b', messages=[
      {"role": "user", "content": parsedData},
      {"role": "user", "content": "You are a formatter. Obey output rules exactly. Analyze the given Python code and describe what each function does. Output only a list of one-line explanations. Each line must begin with a # and contain no extra symbols, no function names, and no bullet points."}])
with open("comments.txt", "w") as output:
    output.write(response['message']['content'])

# Send the generated comments to the commentInserter service using TCP socket connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(("inserter", 7777))
client.connect(("localhost", 7777))

file = open('comments.txt', 'r')

client.send(file.read().encode())

file.close()
client.close()