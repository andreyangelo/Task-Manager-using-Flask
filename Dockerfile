FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_DEBUG=False
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=8080

EXPOSE 8080

CMD ["python", "todo_project/run.py"]
