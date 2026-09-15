# FinTrust Cloud Portfolio

**Learner:** Tshifhiwa Ramukhadi  
**Programme:** Cloud to Solutions Accelerator (16 Weeks)  
**Target Certification:** AWS Certified Solutions Architect – Associate (SAA-C03)  
**Cohort Start:** 6 July 2026

---

# About This Repository

This portfolio documents my work throughout the 16-week Cloud to Solutions Accelerator Programme.

Each weekly folder contains hands-on technical exercises, architecture decisions, SQL scripts, Python applications, cloud labs, automation projects, and supporting documentation built around the FinTrust Bank case study.

The project simulates a South African digital banking environment deployed in the AWS Africa (Cape Town) Region (`af-south-1`), applying real-world cloud architecture, networking, security, automation, migration, governance, SQL analytics, and data engineering concepts.

---

# Week 02: Compute, SQL Aggregates & Python Fundamentals

## What I Built

SQL queries demonstrating:

- INNER JOIN
- LEFT JOIN
- GROUP BY
- HAVING

using the FinTrust Bank transactions dataset.

Python applications implementing fraud detection decision engines using:

- if / elif / else
- Boolean logic
- Membership testing
- Early return patterns
- Decimal for financial accuracy

## Key Concepts Demonstrated

### AWS Compute Services

#### Amazon EC2

- Persistent virtual servers
- Long-running workload hosting

#### AWS Lambda

- Event-driven serverless execution
- Pay-per-use compute

#### Amazon ECS

- Container orchestration
- Microservice deployment

### Storage

#### gp3 EBS Volumes

- General-purpose SSD storage
- Cost-effective workloads

#### io2 EBS Volumes

- High-performance SSD storage
- Mission-critical workloads

### SQL

- Aggregate Functions
- Joins
- Data Grouping
- HAVING Filters

### Python

- Conditional Logic
- Boolean Expressions
- Membership Operators
- Currency Handling with Decimal
- Fraud Detection Flows

---

# Week 03: Python, Data Processing & Documentation

## What I Built

- Python automation exercises
- Data processing workflows
- Decision-tree applications
- Technical reflections
- Architecture documentation

## Key Concepts Demonstrated

- Python Functions
- File Handling
- Logging
- Documentation
- Data Processing
- Automation

---

# Week 04: Data Engineering and SQLite Reporting Pipeline

## What I Built

- CSV ingestion workflows
- SQLite database creation
- ETL pipelines
- Reporting queries
- Data validation processes

## Key Concepts Demonstrated

### Data Engineering

- CSV Processing
- Database Design
- SQLite Administration
- Data Transformation
- Reporting Automation

### SQL

- Aggregations
- Reporting Queries
- Data Analysis

### Python

- ETL Concepts
- Database Connectivity
- File Processing
- Error Handling

---

# Week 05: AWS Networking, Connectivity and DNS

## What I Built

### Day 1 – Multi-AZ VPC Architecture

- Multi-AZ VPC Design
- Internet Gateway Architecture
- NAT Gateway Design
- Security Group Design
- Route Table Configuration

### Day 2 – Connectivity and Load Balancing

- Application Load Balancer Design
- Path-Based Routing
- Transit Gateway Exercises
- PrivateLink Evaluation
- Hybrid Connectivity Design

### Day 3 – Route 53 and DNS

- Hosted Zones
- Alias Records
- CNAME Records
- Weighted Routing
- Canary Deployment Routing

## Key Concepts Demonstrated

### Networking

- VPC Design
- CIDR Planning
- Route Tables
- Security Groups
- Public and Private Subnets

### Connectivity

- Transit Gateway
- VPC Peering
- PrivateLink
- Direct Connect
- AWS Client VPN

### Load Balancing

- Application Load Balancer
- Layer 7 Routing
- Target Groups
- TLS Concepts

### DNS

- Route 53
- Alias Records
- CNAME Records
- Routing Policies

---

# Week 06: Security, IAM and Monitoring Automation

## What I Built

- IAM security exercises
- Security group auditing tools
- CloudWatch monitoring scripts
- Compliance reporting tools
- Security automation projects

## Key Concepts Demonstrated

### Security

- IAM Policies
- Least Privilege Access
- Security Groups
- Compliance Controls

### Monitoring

- CloudWatch Metrics
- CloudWatch Alarms
- Dashboard Concepts

### Python

- boto3 Security Auditing
- Compliance Reporting
- Monitoring Automation

---

# Week 07: Serverless and API Development

## What I Built

- Lambda functions
- API integrations
- Event-driven workflows
- Serverless applications

## Key Concepts Demonstrated

### Serverless

- AWS Lambda
- API Gateway
- EventBridge
- SNS

### Python

- Lambda Handlers
- Event Processing
- API Development

---

# Week 08: Streaming, AI Services and Data Engineering

## What I Built

- Kinesis producers and consumers
- OpenSearch integrations
- CSV to Parquet ETL pipelines
- Comprehend PII redaction workflows
- Face verification solutions
- AI processing pipelines

## Key Concepts Demonstrated

### Data Engineering

- Amazon Kinesis
- OpenSearch
- Amazon S3
- Apache Parquet

### Artificial Intelligence

- Amazon Comprehend
- PII Detection
- NLP Services

### Python

- ETL Automation
- Streaming Data Processing
- AI Workflow Development

---

# Week 09: Cost Optimisation and Governance

## What I Built

- Cost Explorer reports
- Budget monitoring tools
- Savings Plan calculators
- TCO analysis models
- Governance reporting
- Tag compliance auditors

## Key Concepts Demonstrated

### Cost Optimisation

- AWS Pricing Models
- Cost Explorer
- AWS Budgets
- Savings Plans

### Governance

- Tagging Standards
- Resource Compliance
- Cost Allocation

### Python

- Cost Reporting
- Governance Automation
- Financial Analysis

---

# Week 10: Migration Automation and SQL Reporting

## What I Built

### Python Migration Package

```text
fintrust_migration/
├── utils/
│   └── sessions.py
├── ec2/
│   └── classifier.py
├── rds/
│   └── dms_helpers.py
├── s3/
│   └── sync_helpers.py
└── __init__.py
```

### Migration Automation

- EC2 workload classification
- Migration wave identification
- DMS monitoring and automation
- CDC lag monitoring
- DataSync task automation
- Dynamic bandwidth throttling

### SQL Reporting

Created reporting views including:

- Wave Progress
- Portfolio Completion
- Customer Account Summary
- Monthly Transaction Summary
- Daily Transfer Volume
- Migration Progress Reporting
- Transfer Audit Reporting

## Key Concepts Demonstrated

### Migration Services

- AWS Migration Strategies (6Rs)
- AWS DMS
- AWS DataSync
- EventBridge Scheduler

### Python

- Package Development
- boto3 Automation
- Monitoring and Orchestration

### SQL

- Views
- Reporting Queries
- Aggregations
- Audit Reporting

---

# Week 11: SQL Analytics and Window Functions

## What I Built

- Window Function exercises
- Ranking analysis queries
- Running totals
- Moving averages
- Lead and Lag analysis
- Quartile segmentation

## Key Concepts Demonstrated

### SQL Window Functions

- OVER()
- PARTITION BY
- ORDER BY

### Ranking Functions

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

### Analytical Functions

- LAG()
- LEAD()
- NTILE()

### Reporting

- Trend Analysis
- Financial Analytics
- Business Intelligence Queries

---

# Architecture Context

All FinTrust deliverables form part of a simulated digital banking platform running in the AWS Africa (Cape Town) Region (`af-south-1`).

Architecture decisions align with the AWS Well-Architected Framework:

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability

---

# Skills Demonstrated

### Cloud Architecture

- AWS Well-Architected Design
- Multi-Tier Architectures
- Hybrid Connectivity

### Networking

- VPC Design
- DNS
- Load Balancing
- Hybrid Connectivity

### Security

- IAM
- Monitoring
- Compliance Controls

### Data Engineering

- SQL Analytics
- ETL Pipelines
- Streaming Data

### Application Development

- Python
- Serverless Computing
- Automation

### Migration

- AWS DMS
- AWS DataSync
- Cloud Migration Planning

### Analytics

- SQL Views
- Window Functions
- Business Intelligence Reporting

---

# Progress Tracker

| Week | Theme | Status |
|--------|--------|--------|
| Week 1 | Foundation | ✅ Completed |
| Week 2 | Compute, SQL & Python Fundamentals | ✅ Completed |
| Week 3 | Python, Data Processing & Documentation | ✅ Completed |
| Week 4 | SQLite Reporting Pipeline | ✅ Completed |
| Week 5 | AWS Networking, Connectivity & DNS | ✅ Completed |
| Week 6 | Security, IAM & Monitoring | ✅ Completed |
| Week 7 | Serverless & API Development | ✅ Completed |
| Week 8 | Streaming, AI & Data Engineering | ✅ Completed |
| Week 9 | Cost Optimisation & Governance | ✅ Completed |
| Week 10 | Migration Automation & SQL Reporting | ✅ Completed |
| Week 11 | SQL Analytics & Window Functions | 🚧 In Progress |
| Week 12 | Coming Soon | ⏳ Planned |
| Week 13 | Coming Soon | ⏳ Planned |
| Week 14 | Coming Soon | ⏳ Planned |
| Week 15 | Coming Soon | ⏳ Planned |
| Week 16 | Capstone & Certification Preparation | ⏳ Planned |

---

# Goal

Develop practical cloud engineering, architecture, automation, migration, governance, and data engineering skills while preparing for:

## AWS Certified Solutions Architect – Associate (SAA-C03)

This portfolio demonstrates hands-on experience in:

- Cloud Architecture
- Networking
- Security
- Automation
- Python Development
- SQL Analytics
- Data Engineering
- Migration Engineering
- Cost Optimisation
- Governance
- Business Intelligence Reporting

while building solutions aligned to real-world enterprise cloud environments.