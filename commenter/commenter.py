import socket
import anthropic

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
client = anthropic.Anthropic()

function_names = []

for lines in parsedData:
    if "functionName" in lines:
        function_names.append(lines[22:-1].strip())

prompt = f"""
You are documenting Python code.

For each function name below, write ONE single-line Python comment.

Rules:
- Each comment must start with "# "
- Output exactly one comment per function
- Keep comments under 100 characters
- No explanations
- Return comments in the SAME ORDER as the functions

Functions:
{function_names}
"""

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=2000,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

comments = response.content[0].text.strip().split("\n")

with open("comments.txt", "w") as commentsFile:
    for comment in comments:
        if not comment.startswith("#"):
            comment = "# " + comment
        commentsFile.write(comment + "\n")

# Send the generated comments to the commentInserter service using TCP socket connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("inserter", 7777))
#client.connect(("localhost", 7777))

file = open('comments.txt', 'r')

client.send(file.read().encode())

file.close()
client.close()