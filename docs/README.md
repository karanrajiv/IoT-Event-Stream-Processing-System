
# IoT Event Stream Processing System

This project simulates and processes real-time IoT sensor data using Kafka, Spark Streaming, Redis, FastAPI, and Streamlit. It includes a data ingestion pipeline, streaming processor, REST API, and live dashboard for monitoring alerts.

## 🚀 Features

- **Kafka Producer**: Generates mock temperature/humidity readings from virtual sensors.
- **Kafka Consumer**: Monitors the stream and pushes high-temperature alerts to Redis.
- **Spark Streaming**: Parses and displays streaming sensor data in real-time.
- **FastAPI**: Exposes a REST API to query historical alerts.
- **Streamlit Dashboard**: Live visualization of alerts and sensor trends.
- **GitHub Actions CI**: Linting workflow for Python codebase.

## 🧰 Tech Stack

- Apache Kafka, Zookeeper
- Apache Spark (Structured Streaming)
- Redis
- FastAPI, Streamlit
- Docker, Docker Compose
- Python 3.9

## 📁 Project Structure

```
.
├── api/                  # FastAPI server
│   └── main.py
├── consumer/             # Kafka consumer
│   └── consumer.py
├── dashboard/            # Streamlit app
│   └── app.py
├── docker/               # Docker Compose setup
│   └── docker-compose.yml
├── docs/                 # Documentation
│   └── README.md
├── producer/             # Kafka producer
│   └── producer.py
├── streaming/            # Spark Streaming job
│   └── streaming_job.py
└── .github/
    └── workflows/
        └── ci.yml        # GitHub Actions workflow
```

## 🧪 How to Run

### 1. Start the Infrastructure
```bash
docker-compose -f docker/docker-compose.yml up -d
```

### 2. Start Components
```bash
# Terminal 1 - Start Kafka Producer
python producer/producer.py

# Terminal 2 - Start Kafka Consumer
python consumer/consumer.py

# Terminal 3 - Start Spark Streaming Job
spark-submit streaming/streaming_job.py

# Terminal 4 - Start FastAPI Server
uvicorn api.main:app --reload

# Terminal 5 - Run Streamlit Dashboard
streamlit run dashboard/app.py
```

## 🌡️ Alert Logic

- Temperature > 30°C triggers an alert
- Alerts are stored in Redis under the key `alerts`
- Retrieved via API or visualized in the dashboard

## 🧪 CI Integration

GitHub Actions runs linting using `flake8` on all Python files on every push to `main`.

## 📬 API Endpoint

- `GET /alerts` - returns all stored alerts as JSON

## 📊 Dashboard

The dashboard continuously polls Redis and displays:
- Real-time temperature and humidity line chart
- Tabular view of recent alerts

## 📝 License

MIT License
