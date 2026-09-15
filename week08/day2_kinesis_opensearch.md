# Week 8 Day 2 PM: Real-Time Data Pipelines with Kinesis and OpenSearch

## Objective

Build real-time transaction pipelines using:

- Kinesis Data Streams
- AWS Lambda
- OpenSearch
- boto3

---

## Kinesis Producer

Service:

AWS Kinesis Data Streams

Purpose:

Publish real-time transaction events.

Example event:

```json
{
  "transaction_id": "txn-001",
  "account_id": "ACC-0001",
  "amount": 5000,
  "currency": "ZAR"
}
```

---

## Partition Key Strategy

Partition key:

```text
account_id
```

Benefits:

- Preserves ordering
- Keeps all transactions for an account together
- Supports fraud pattern detection

---

## Kinesis Batch Processing

Method:

```python
put_records()
```

Benefits:

- Better throughput
- Fewer API calls
- Lower latency

---

## OpenSearch

Purpose:

Store and search security and transaction events.

Example event:

```json
{
  "event_type": "SUSPICIOUS_LOGIN",
  "risk_score": 87
}
```

Capabilities:

- Full-text search
- Log analytics
- Security monitoring
- Dashboard visualisation

---

## Lambda Kinesis Consumer

Responsibilities:

1. Receive records from Kinesis
2. Decode Base64 payload
3. Parse JSON
4. Process fraud events
5. Index into OpenSearch

---

## FinTrust Streaming Architecture

```text
Transaction API
       |
       v
Kinesis Data Stream
       |
       v
Lambda Consumer
       |
       v
OpenSearch
       |
       v
Fraud Monitoring Dashboard
```

---

## Reflection: Partition Key Strategy

Using account_id as a partition key preserves transaction ordering for a specific account, which is important for fraud analysis and behavioural pattern detection.

However, if one account generates a very large number of transactions in a short period, all traffic will be directed to a single shard, creating a hot shard problem.

One alternative would be:

```text
account_id + timestamp bucket
```

or

```text
account_id + random suffix
```

This would distribute the load across multiple shards and improve throughput.

The trade-off is that strict ordering for all transactions belonging to one account would no longer be guaranteed.