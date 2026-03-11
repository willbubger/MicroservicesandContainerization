FROM python:3.12-slim

RUN pip install anthropic
WORKDIR /app
COPY commenter.py .

EXPOSE 9999
CMD ["python3", "commenter.py"]
