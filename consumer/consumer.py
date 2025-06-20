
import json
from kafka import KafkaConsumer
import redis

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

redis_client = redis.Redis(host='localhost', port=6379, db=0)

for message in consumer:
    data = message.value
    print(f"Consumed: {data}")
    if data['temperature'] > 30:
        redis_client.rpush('alerts', json.dumps(data))
        print(f"Alert stored: {data}")
