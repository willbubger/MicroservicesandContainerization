with open("/users/willreed/desktop/demo.py", "r") as file, open("comments.txt", "r") as comments:
    data = file.readlines()
    comments = comments.read().splitlines()

output = []
for line in data:
    if line.strip().startswith("def "):
        output.append(comments.pop(0) + "\n")
    output.append(line)

with open("demoCommented.py", "w") as finalOutput:
    finalOutput.writelines(output)