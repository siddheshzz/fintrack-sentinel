# FinTrack-Sentinel 🛡️
Real-time Fraud & Anomaly Detection System

FinTrack-Sentinel is a learning project for high-scale microservices ecosystem built to ingest, validate, and monitor financial transactions in real-time. It demonstrates the transition from a traditional monolithic "Bank App" to an Event-Driven Architecture.

### The Architecture
The system is split into three decoupled services:

**Transaction Service (Ingestion):** A FastAPI gateway that validates incoming JSON payloads and pushes them into a Redis Stream for sub-millisecond handoff.

**Validation Service (The Processor):** A background worker that consumes the queue, executing a "Fraud Engine" (checking IP blacklists, transaction velocity, and high-value thresholds).

**Notification Service (Observability):** Uses Python Generators to stream live security logs to an Admin Dashboard via Server-Sent Events (SSE).

### 🛠️ Tech Stack
**Language**: Python 3.12+ (managed by uv)

**Framework**: FastAPI (Asynchronous I/O)

**Data Store**: PostgreSQL (Relational persistence)

**Messaging**: Redis (Pub/Sub & Streams)

**Infrastructure**: Docker, AWS ECS (Elastic Container Service)

### The Transaction Model
```Python

{
  "txn_id": "uuid-v4",
  "user_id": "user_123",
  "amount": 150000.00,
  "currency": "INR",
  "merchant_type": "luxury_goods",
  "source_ip": "192.168.1.50",
  "status": "PENDING"
}
```
### Challenges Addressed
**Decoupling**: The API doesn't wait for fraud checks to finish. This ensures the user experience is never slowed down by complex backend logic.

**Concurrency**: Used asyncio and uvloop to handle thousands of concurrent connections.

**Memory Efficiency**: Implemented Python Generators (yield) in the Notification service to stream logs without loading the entire DB into memory.

**Scalability**: The Validation Service is designed to be "stateless," allowing us to spin up 10+ workers during peak hours (e.g., Black Friday).

### Getting Started
Clone the repo.

Run docker-compose up --build.

Send a test transaction:

```Bash

curl -X POST http://localhost:8001/transactions -d '{"amount": 200000, "source_ip": "12.34.56.78"}'
```
