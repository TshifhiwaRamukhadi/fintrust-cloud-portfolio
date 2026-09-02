# Week 7 Day 4 PM: Event-Driven Transaction Scoring Pipeline

## Objective

Build an event-driven fraud detection pipeline using:

- Flask
- SQS
- Lambda
- SNS
- boto3

---

## Architecture

```text
Flask API
   ↓
SQS FIFO Queue
   ↓
Lambda Fraud Scorer
   ↓
SNS Alert Topic
   ↓
Compliance Consumer
```

---

## Client vs Resource

### Client

Low-level API interface.

Examples:

```python
sqs = boto3.client("sqs")
sns = boto3.client("sns")
```

Used for:

- SQS
- SNS
- EventBridge

### Resource

Higher-level object interface.

Example:

```python
s3 = boto3.resource("s3")
```

Used for:

- S3
- EC2
- DynamoDB

---

## SQS Producer

Transactions are sent to an SQS FIFO queue.

Important settings:

```python
MessageGroupId
```

Maintains ordering.

```python
MessageDeduplicationId
```

Prevents duplicate processing.

---

## Fraud Scoring Logic

### Amount Rules

| Amount | Score |
|----------|--------|
| > 50 000 | 40 |
| > 10 000 | 20 |
| > 1 000 | 5 |

### Currency Rule

Non-ZAR:

```text
+20
```

### Keyword Rule

Keywords:

```text
crypto
wire
urgent
casino
```

Adds:

```text
+15
```

---

## SNS Alerts

Alerts are published when:

```text
Risk Score >= 75
```

SNS message contains:

- transaction_id
- account_id
- amount
- currency
- risk_score

---

## Reflection: Pipeline Gaps

If the Lambda function throws an unhandled exception, message processing fails and SQS retries the message.

With ReportBatchItemFailures enabled, Lambda reports only the failed records and SQS retries those specific messages rather than the entire batch.

To make the solution production-ready, I would add an SQS Dead Letter Queue (DLQ). Messages that repeatedly fail processing would be moved to the DLQ instead of being retried indefinitely. This prevents poisoned messages from blocking the queue and provides a location for investigation and recovery.