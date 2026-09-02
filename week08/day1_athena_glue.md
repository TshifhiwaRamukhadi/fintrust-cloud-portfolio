# Week 8 Day 1 PM: Athena and Glue with Python

## Objective

Learn how to query Athena programmatically and inspect metadata stored in the Glue Data Catalog.

---

## Athena Client

Athena uses the boto3 client pattern.

```python
athena = boto3.client(
    "athena",
    region_name="af-south-1"
)
```

---

## Athena Execution Model

Athena is asynchronous.

Steps:

1. Submit query
2. Receive QueryExecutionId
3. Poll execution status
4. Retrieve results

Possible states:

- QUEUED
- RUNNING
- SUCCEEDED
- FAILED
- CANCELLED

---

## Why Athena Is Asynchronous

Athena queries may scan terabytes of Parquet data stored in Amazon S3.

Returning data synchronously would cause HTTP timeouts and poor scalability.

---

## Glue Data Catalog

The Glue Catalog stores:

- Databases
- Tables
- Schemas
- Partition definitions

It acts as a central metadata repository for:

- Athena
- EMR
- Redshift Spectrum
- Glue ETL

---

## Partitioning

Example:

```sql
WHERE year = '2024'
AND month = '06'
```

Benefits:

- Reads fewer files
- Faster execution
- Lower Athena costs

---

## FinTrust Compliance Reporter

Capabilities:

- Executes Athena queries
- Polls automatically
- Writes CSV reports
- Uploads reports to S3

---

## Reflection: Sync vs Async APIs

Athena follows an asynchronous execution model because queries may process large datasets across many files stored in Amazon S3.

Glue catalog operations are synchronous because metadata retrieval is relatively small and completes quickly.

Another AWS service that follows an asynchronous pattern is AWS Lambda when triggered through SQS. Messages are submitted to the queue and processed later instead of returning an immediate business result. This design is more practical when handling large volumes of transactions because it improves scalability and prevents client timeouts.