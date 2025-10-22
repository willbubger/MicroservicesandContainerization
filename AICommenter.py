from ollama import chat
from ollama import ChatResponse

with open("/Users/willreed/PycharmProjects/PythonCodeParser/parsed.json", 'r') as file:
    content = file.read()

response: ChatResponse = chat(model='gemma3:1b', messages=[
      {"role": "user", "content": content},
      {"role": "user", "content": "You are a formatter. Obey output rules exactly. Analyze the given Python code and describe what each function does. Output only a list of one-line explanations. Each line must begin with a # and contain no extra symbols, no function names, and no bullet points."}
])
with open("comments.txt", "w") as output:
    output.write(response['message']['content'])