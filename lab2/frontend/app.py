from flask import Flask
import redis
import os

app = Flask(__name__)

# Подключение к Redis через имя сервиса
redis_host = os.getenv('REDIS_HOST', 'redis-service')
redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)

# Цвет фона из переменной окружения (по умолчанию белый)
BACKGROUND_COLOR = os.getenv('BACKGROUND_COLOR', '#ffffff')

@app.route('/')
def index():
    count = redis_client.incr('hits')
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Счетчик посещений</title>
        <style>
            body {{
                background-color: {BACKGROUND_COLOR};
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                padding: 40px;
                border-radius: 15px;
                background-color: rgba(255, 255, 255, 0.8);
                box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            }}
            h1 {{
                color: #333;
            }}
            .count {{
                font-size: 3em;
                color: #007bff;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Привет из Kubernetes!</h1>
            <p>Количество посещений:</p>
            <div class="count">{count}</div>
            <p>Версия: v1 (белый фон)</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)