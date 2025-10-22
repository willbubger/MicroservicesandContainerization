FROM python:3.11-slim
WORKDIR /Users/willreed/PycharmProjects/PythonCodeParser
COPY . .
EXPOSE 8080
RUN pip install ollama
CMD ["python", "pythonParser.py"]