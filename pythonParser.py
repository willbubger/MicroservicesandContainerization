import ast, json

def parseCode(code):
    tree = ast.parse(code)
    result = {"functions": []}

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

file = open("/users/willreed/desktop/demo.py")

with open("parsed.json", "w") as f:
    json.dump(parseCode(file.read()), f, indent=2)
