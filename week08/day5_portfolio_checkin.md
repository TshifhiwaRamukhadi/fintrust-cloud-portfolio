# Week 8 Day 5 PM: Portfolio Check-In #8

## Portfolio Summary

Week 8 focused on analytics, data engineering, streaming architectures, and AI/ML services within the FinTrust platform.

The objective was to demonstrate both architecture design and implementation using Python and AWS services.

---

# Week 8 Deliverables

## Day 1: Athena and Glue

Files:

- athena_query_runner.py
- glue_catalog_inspector.py
- fintrust_compliance_reporter.py

Skills demonstrated:

- Athena query execution
- Query polling
- Glue Data Catalog inspection
- Compliance reporting
- CSV report generation

Business value:

FinTrust compliance teams can generate transaction monitoring reports directly from data lake storage without maintaining a traditional reporting database.

---

## Day 2: Kinesis and OpenSearch

Files:

- kinesis_producer.py
- kinesis_batch_producer.py
- opensearch_indexer.py
- lambda_kinesis_decoder.py

Skills demonstrated:

- Real-time streaming
- Partition key design
- OpenSearch indexing
- Event-driven processing
- Batch publishing

Business value:

FinTrust fraud monitoring systems can process transaction events in near real time and surface suspicious patterns more quickly.

---

## Day 3: Pandas, Parquet and S3

Files:

- csv_to_parquet_etl.py
- s3_parquet_upload.py
- parquet_analysis.py

Skills demonstrated:

- Pandas transformations
- ETL pipelines
- Partitioned Parquet datasets
- S3 integration
- Data aggregation

Business value:

FinTrust analytics workloads operate more efficiently by storing transaction history in Parquet format rather than large CSV files.

---

## Day 4: Rekognition and Comprehend

Files:

- kyc_face_verification.py
- comprehend_pii_redaction.py
- support_ticket_processor.py

Skills demonstrated:

- Rekognition CompareFaces
- KYC verification workflows
- PII detection
- Sentiment analysis
- Automated support routing

Business value:

FinTrust can automate customer onboarding and support ticket handling while improving regulatory compliance.

---

# Analytics Architecture

```text
Transaction Sources
        |
        v
Amazon S3 Data Lake
        |
        v
AWS Glue Catalog
        |
        v
Amazon Athena
        |
        v
Amazon QuickSight
```

Purpose:

- Centralised analytics
- Compliance reporting
- Executive dashboards
- Regulatory auditing

---

# Streaming Architecture

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
Fraud Dashboard
```

Purpose:

- Real-time fraud monitoring
- Operational visibility
- Security analytics

---

# AI and ML Architecture

```text
Customer Upload
       |
       v
Amazon S3
       |
       v
Rekognition CompareFaces
       |
       v
KYC Decision

Support Ticket
       |
       v
Comprehend
       |
       v
PII Redaction
       |
       v
Sentiment Routing
       |
       v
Amazon SQS
```

Purpose:

- Identity verification
- Support automation
- POPIA compliance
- Reduced manual processing

---

# FinTrust Narrative

Week 8 extended FinTrust from a transaction platform into an analytics and intelligent decision-making platform.

Athena and Glue support compliance reporting and allow analysts to query large-scale transaction datasets stored in the FinTrust data lake.

Kinesis and OpenSearch add real-time monitoring capabilities so fraud and security teams can investigate suspicious events as they occur.

Parquet-based ETL pipelines reduce query costs and improve performance by optimising how transaction data is stored and processed.

Rekognition strengthens customer identity verification during onboarding through facial comparison workflows, while Comprehend assists customer support teams by detecting PII and prioritising urgent requests automatically.

Together these services create a platform capable of supporting compliance, fraud prevention, customer onboarding, operational monitoring and data-driven decision making.

---

# GitHub Evidence

Week 8 commits:

```text
W8D1: Athena and Glue reporting automation
W8D2: Kinesis streaming and OpenSearch integration
W8D3: Pandas Parquet and S3 ETL pipeline
W8D4: Rekognition and Comprehend AI pipelines
```

These commits demonstrate continuous development and implementation throughout the week.

---

# Week 9 Preparation

## Pricing Models

### On-Demand

- No commitment
- Highest flexibility
- Highest cost

### Reserved Instances

- 1 or 3 year commitment
- Significant savings
- Predictable workloads

### Spot Instances

- Lowest cost
- Interruptible
- Suitable for batch workloads

---

## Savings Plans

Provide flexibility while reducing compute costs.

Useful for:

- Lambda
- ECS
- EC2

---

## Migration Strategies (7 Rs)

- Retire
- Retain
- Rehost
- Replatform
- Repurchase
- Refactor
- Relocate

---

## DR Strategies

### Backup and Restore

Lowest cost.

### Pilot Light

Critical services always running.

### Warm Standby

Reduced-scale environment continuously running.

### Active-Active

Highest availability and highest cost.

---

# Week 8 Reflection

One of the most cost-driven decisions made during Week 8 was the adoption of Parquet rather than CSV for analytics workloads. Athena pricing is based on the amount of data scanned, so storing large FinTrust transaction datasets in CSV would increase query costs significantly because every query would need to scan entire files regardless of which columns were required. By converting data into the Parquet format and partitioning it by year and month, Athena can scan only the required columns and partitions. This dramatically reduces both cost and execution time. The trade-off is additional ETL complexity because data must first be transformed and written into Parquet format before becoming available for analytics. There is also a requirement to maintain schema consistency and partition structures correctly. Despite this additional engineering effort, the savings achieved at scale make Parquet the preferred option for FinTrust. The reduction in storage requirements, faster query performance, and lower Athena charges outweigh the operational overhead required to maintain the ETL pipeline.