from flask import Flask
import redis
import os

app = Flask(__name__)

# Подключение к Redis через имя сервиса (service discovery)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    # Увеличиваем счетчик посещений
    count = redis_client.incr('hits')
    return f'<h1>Привет! Количество посещений: {count}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)