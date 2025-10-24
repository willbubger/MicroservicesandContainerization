FROM python:3.12-slim

RUN pip install ollama
WORKDIR /app
COPY AICommenter.py .

ENV OLLAMA_HOST=http://host.docker.internal:11434

EXPOSE 9999
CMD ["python3", "AICommenter.py"]
