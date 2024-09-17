FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD flask --app Backend_Labs_2024/views.py run --host 0.0.0.0 --port $PORT
