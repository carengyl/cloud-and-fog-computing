import paho.mqtt.client as mqtt
import json
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print("✅ Cloud Dashboard подключен к MQTT брокеру")
    client.subscribe("factory/alerts/high_temperature")

def on_message(client, userdata, msg):
    """Обработка критических алертов"""
    try:
        data = json.loads(msg.payload.decode())
        timestamp = datetime.fromtimestamp(data['timestamp']).strftime('%H:%M:%S')
        
        print(f"""
        🚨 КРИТИЧЕСКОЕ СОБЫТИЕ 🚨
        Время: {timestamp}
        Датчик: {data['sensor_id']}
        Температура: {data['temperature']}°C
        Топик: {msg.topic}
        """)
        
        # Здесь можно добавить запись в БД, отправку email, etc.
        
    except Exception as e:
        print(f"❌ Ошибка обработки сообщения: {e}")

def main():
    client = mqtt.Client("cloud-dashboard")
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect("mosquitto", 1883, 60)
    client.loop_forever()

if __name__ == "__main__":
    print("🌥 Cloud Dashboard запущен...")
    print("Ожидание критических алертов (температура > 80°C)...")
    main()