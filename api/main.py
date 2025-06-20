
from fastapi import FastAPI
import redis
import json

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/alerts")
def get_alerts():
    alerts = r.lrange("alerts", 0, -1)
    return [json.loads(alert) for alert in alerts]
