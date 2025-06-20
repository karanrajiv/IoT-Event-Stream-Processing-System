
import streamlit as st
import redis
import json
import pandas as pd
import time

st.set_page_config(page_title='IoT Alert Dashboard', layout='wide')
st.title("📡 IoT Sensor Alert Dashboard")

redis_client = redis.Redis(host='localhost', port=6379, db=0)

placeholder = st.empty()

def fetch_alerts():
    alerts = redis_client.lrange("alerts", 0, -1)
    return [json.loads(alert) for alert in alerts]

while True:
    with placeholder.container():
        alerts = fetch_alerts()
        if alerts:
            df = pd.DataFrame(alerts)
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
            st.line_chart(df.set_index('timestamp')[['temperature', 'humidity']])
            st.dataframe(df.sort_values(by='timestamp', ascending=False), use_container_width=True)
        else:
            st.info("No alerts available.")
    time.sleep(5)
