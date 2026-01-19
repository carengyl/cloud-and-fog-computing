import paho.mqtt.client as mqtt
import time
import random
import json
import os

# Конфигурация MQTT
MQTT_BROKER = os.getenv("MQTT_BROKER", "mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = "factory/sensor/temperature"
SENSOR_ID = os.getenv("SENSOR_ID", "sensor-01")

client = mqtt.Client(client_id=SENSOR_ID)

def connect_mqtt():
    """Подключение к MQTT брокеру"""
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print(f"✅ Датчик {SENSOR_ID} подключен к {MQTT_BROKER}:{MQTT_PORT}")
        return client
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return None

def publish_temperature():
    """Публикация случайной температуры каждую секунду"""
    while True:
        # Генерация температуры от 20°C до 100°C
        temperature = random.uniform(20.0, 100.0)
        
        # Формирование сообщения
        message = {
            "sensor_id": SENSOR_ID,
            "temperature": round(temperature, 2),
            "timestamp": time.time(),
            "unit": "celsius"
        }
        
        # Публикация в MQTT
        result = client.publish(
            MQTT_TOPIC, 
            json.dumps(message), 
            qos=1
        )
        
        status = "✅" if result.rc == mqtt.MQTT_ERR_SUCCESS else "❌"
        print(f"{status} {SENSOR_ID}: {temperature:.1f}°C")
        
        time.sleep(1)

if __name__ == "__main__":
    mqtt_client = connect_mqtt()
    if mqtt_client:
        mqtt_client.loop_start()
        publish_temperature()