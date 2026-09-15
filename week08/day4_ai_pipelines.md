# Week 8 Day 4 PM: AI Pipelines with Rekognition and Comprehend

## Objective

Build AI-powered FinTrust processes using:

- Amazon Rekognition
- Amazon Comprehend
- Amazon SQS
- boto3

---

## Rekognition

Purpose:

Customer identity verification (KYC).

Client:

```python
rek = boto3.client(
    "rekognition",
    region_name="af-south-1"
)
```

---

## CompareFaces

Compares:

- Customer selfie
- ID document photograph

Possible outcomes:

### APPROVE

Similarity ≥ 95%

### MANUAL_REVIEW

Face match found but below threshold.

### REJECT

No match found.

---

## Why 95%?

FinTrust prioritizes prevention of fraud and identity theft.

False positives create higher risk than manual reviews.

---

## Comprehend

Purpose:

Natural language processing.

Capabilities:

- PII detection
- Sentiment analysis
- Entity recognition

---

## PII Redaction

Examples of protected information:

- ID numbers
- Phone numbers
- Names
- Account numbers

Example output:

```text
My name is [NAME]
and my ID is [ID]
```

---

## Sentiment Analysis

Possible sentiments:

```text
POSITIVE
NEGATIVE
NEUTRAL
MIXED
```

Used to prioritize support requests.

---

## Support Ticket Routing

Workflow:

```text
Support Ticket
       |
       v
Comprehend
(PII + Sentiment)
       |
       v
Routing Decision
       |
       +----------------+
       |                |
       v                v
Standard Queue   Urgent Queue
```

---

## FinTrust KYC Architecture

```text
Customer Upload
       |
       v
Amazon S3
       |
       v
Lambda
       |
       v
Rekognition CompareFaces
       |
       +-------------------+
       |                   |
       v                   v
APPROVE       MANUAL_REVIEW / REJECT
```

---

## IAM Permissions

### Rekognition Function

Required permissions:

```text
rekognition:CompareFaces
s3:GetObject
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
```

Scope:

- KYC upload bucket
- Lambda log group

---

### Support Ticket Processor

Required permissions:

```text
comprehend:DetectPIIEntities
comprehend:DetectSentiment
sqs:SendMessage
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
```

Scope:

- fintrust-support-urgent queue
- fintrust-support-standard queue

---

## Reflection

The support ticket processor would typically be triggered through API Gateway when a customer submits a ticket through the FinTrust support portal.

The Lambda execution role should follow least-privilege principles and include only the exact Comprehend, SQS and CloudWatch permissions required to process and route support tickets.