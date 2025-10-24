import ast, json, socket, time

# Give the AICommenter and commentInserter time to start
#time.sleep(5)

# Utilizing the AST module, we parse the Python code to extract function definitions and their details.
def parseCode(code):
    tree = ast.parse(code)
    result = {"functions": []}

    # Walk through the AST nodes to find function definitions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_info = {
                "name": node.name,
                "args": [arg.arg for arg in node.args.args],
                "returns": node.returns,
                "start": node.lineno,
                "end": node.end_lineno
            }
            result["functions"].append(func_info)
    return result

file = open("demo.py")

# Parse the code and save the structured data to parsed.json
with open("parsed.json", "w") as f:
    json.dump(parseCode(file.read()), f, indent=2)

# Send the parsed data to the AICommenter service using TCP socket connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(("commenter", 9999))
client.connect(("localhost", 9999))

file = open('parsed.json', 'r')

client.send(file.read().encode())
print("Sent parsed data")

file.close()
client.close()
