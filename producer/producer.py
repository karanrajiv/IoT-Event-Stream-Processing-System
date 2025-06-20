
import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data(sensor_id):
    return {
        "sensor_id": sensor_id,
        "timestamp": time.time(),
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 70), 2)
    }

if __name__ == "__main__":
    sensor_ids = ['sensor_1', 'sensor_2', 'sensor_3']
    while True:
        for sensor_id in sensor_ids:
            data = generate_sensor_data(sensor_id)
            producer.send('sensor-data', value=data)
            print(f"Produced: {data}")
        time.sleep(2)
