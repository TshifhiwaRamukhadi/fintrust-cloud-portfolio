# Week 7 Day 5 PM: Portfolio Check-In #7

## Portfolio Summary

Week 7 focused on API development, AWS Lambda execution, and event-driven architecture.

The work completed demonstrates both cloud architecture design and Python implementation skills.

---

# Week 7 Deliverables

## Day 1: Flask and FastAPI

Files:

- flask_app.py
- fastapi_app.py

Skills demonstrated:

- REST API development
- Request validation
- JSON processing
- Route handling
- Pydantic validation
- Swagger documentation

Endpoints created:

- GET /health
- POST /transactions
- GET /transactions
- GET /transactions/{id}
- PATCH /transactions/{id}/status

---

## Day 2: AWS Lambda

Files:

- event_explorer_lambda.py
- fintrust_transaction_lambda.py

Skills demonstrated:

- Lambda handlers
- Event payload processing
- Context object usage
- Environment variables
- Logging
- AWS CLI deployment concepts

---

## Day 4: Event-Driven Fraud Scoring

Files:

- sqs_producer.py
- fraud_scorer_lambda.py

Architecture:

```text
Flask API
    ↓
SQS FIFO Queue
    ↓
Lambda Fraud Scorer
    ↓
SNS Alert Topic
    ↓
Email / Compliance Consumer
```

Skills demonstrated:

- boto3
- SQS messaging
- SNS notifications
- Event-driven architecture
- Risk scoring
- Serverless design

---

# FinTrust Narrative

Week 7 extended the FinTrust payment platform.

New AWS services introduced:

## SQS

Purpose:

Decouple API requests from fraud processing.

Benefit:

The application can continue accepting transactions even when downstream systems are slow.

---

## Lambda

Purpose:

Calculate fraud risk scores automatically.

Benefit:

Serverless execution without managing infrastructure.

---

## SNS

Purpose:

Publish alerts for high-risk transactions.

Benefit:

Multiple compliance systems can subscribe without changing the fraud scorer.

---

# Architecture Justification

## Why SQS?

SQS provides reliable message buffering and decouples services.

The Flask API does not need to wait for fraud analysis before responding to users.

## Why Lambda?

Lambda automatically scales and only runs when messages arrive.

This reduces operational overhead and cost.

## Why SNS?

SNS allows one message to be delivered to multiple consumers simultaneously.

This supports compliance, operations, auditing and monitoring subscribers.

---

# Week 8 Preparation

## Question 1

### Batch Processing vs Stream Processing

Batch processing handles large volumes of data at scheduled intervals.

FinTrust example:

Monthly compliance reports generated from transaction history.

Stream processing handles data continuously as events arrive.

FinTrust example:

Real-time fraud detection on incoming payment transactions.

---

## Question 2

### Data Lake vs Data Warehouse

A data lake stores raw structured and unstructured data.

Examples:

- transaction files
- logs
- JSON events
- CSV exports

A data warehouse stores curated and structured business data optimized for analytics.

Data Lake:

Best when storing large volumes of raw data.

Data Warehouse:

Best when users need fast reporting and business intelligence.

---

## Question 3

### Which File Format Works Best for Athena?

Parquet.

Reasons:

- Columnar storage
- Compression
- Faster queries
- Lower cost because Athena scans less data

---

# Week 7 Reflection

The most significant thing I learned this week was how event-driven architecture solves the problem of tightly coupled applications.

Before learning SQS, Lambda and SNS, I would have designed systems where one service directly called another and waited for a response. This creates bottlenecks and reduces reliability. By introducing SQS between the transaction API and the fraud scorer, transactions can be processed asynchronously and independently. Lambda automatically reacts to events without requiring servers, while SNS distributes alerts to multiple consumers without modifying the producer application. This changed how I think about architecture because I now see messaging services as a way to improve scalability, resilience and maintainability. Instead of building point-to-point integrations, I can design loosely coupled systems that continue operating even when one component is temporarily unavailable. This approach is especially valuable in a banking environment where transaction volumes may increase unexpectedly and fraud detection must scale efficiently.