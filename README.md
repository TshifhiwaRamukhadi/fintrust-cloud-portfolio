# FinTrust Cloud Portfolio

**Learner:** Tshifhiwa Ramukhadi  
**Programme:** Cloud to Solutions Accelerator (16 Weeks)  
**Target Certification:** AWS Certified Solutions Architect – Associate (SAA-C03)  
**Cohort Start:** 6 July 2026

---

# About This Repository

This portfolio documents my work throughout the 16-week Cloud to Solutions Accelerator Programme.

Each weekly folder contains hands-on technical exercises, architecture decisions, SQL scripts, Python applications, cloud labs, and supporting documentation built around the FinTrust Bank case study.

The project simulates a South African digital banking environment deployed in the AWS Africa (Cape Town) Region (`af-south-1`), applying real-world cloud architecture, security, networking, data, and automation concepts.

---

# Week 02: Compute, SQL Aggregates & Python Fundamentals

## What I Built

SQL queries demonstrating:

- INNER JOIN
- LEFT JOIN
- GROUP BY
- HAVING

using the FinTrust Bank transactions dataset.

Python applications implementing a fraud detection decision engine using:

- if / elif / else
- Boolean logic
- Membership testing with the `in` operator
- Early return patterns
- Decimal for currency accuracy

---

## Key Concepts Demonstrated

### AWS Compute Services

#### Amazon EC2

- Persistent virtual servers
- Suitable for long-running workloads

#### AWS Lambda

- Event-driven serverless execution
- Pay only when code runs

#### Amazon ECS

- Container orchestration service
- Ideal for microservices and containerized applications

### Storage

#### gp3 EBS Volumes

- General-purpose SSD storage
- Cost-effective for most workloads

#### io2 EBS Volumes

- High-performance SSD storage
- Designed for mission-critical applications requiring sustained IOPS

### SQL

- Aggregate Functions
- Joins
- Data Grouping
- Filtering with HAVING

### Python

- Conditional Logic
- Boolean Expressions
- Membership Operators
- Currency Handling with Decimal
- Fraud Detection Decision Flows

---

## Project Structure

```text
week02/
│
├── sql/
│   ├── joins_practice.sql
│   └── aggregates_report.sql
│
├── python/
│   ├── conditionals.py
│   └── transaction_flowchart.py
│
└── architecture/
    └── week02_compute_notes.md
```

---

## Files

| File | Description |
|--------|-------------|
| sql/joins_practice.sql | INNER JOIN and LEFT JOIN exercises |
| sql/aggregates_report.sql | Monthly transaction summaries using GROUP BY and HAVING |
| python/conditionals.py | Transaction classifier, interest-rate calculator, and ATM logic |
| python/transaction_flowchart.py | Fraud detection decision engine with five test scenarios |
| architecture/week02_compute_notes.md | Compute service selection and architecture decisions |

---

## How to Run

### SQL Exercises

Requires SQLite:

```bash
sqlite3 :memory: ".read sql/joins_practice.sql"
sqlite3 :memory: ".read sql/aggregates_report.sql"
```

### Python Exercises

```bash
python python/conditionals.py
python python/transaction_flowchart.py
```

---

# Week 03: Python, Data Processing & Documentation

## What I Built

- Python automation exercises
- Data processing workflows
- Decision-tree logic examples
- Technical reflections and documentation
- Supporting diagrams and architecture notes

## Key Concepts Demonstrated

- Python Functions
- File Handling
- Data Processing
- Logging
- Documentation Practices
- Technical Reflection Writing

---

# Week 04: Data Engineering and SQLite Reporting Pipeline

## What I Built

- CSV ingestion workflow
- SQLite database creation
- Automated reporting pipeline
- SQL analysis queries
- Data quality validation

## Key Concepts Demonstrated

### Data Engineering

- CSV Processing
- Database Design
- SQLite Administration
- Data Transformation
- Automated Reporting

### SQL

- Aggregations
- Filtering
- Reporting Queries
- Business Metrics

### Python

- ETL Concepts
- Database Connectivity
- File Processing
- Error Handling

---

# Week 05: AWS Networking, Connectivity and DNS

## What I Built

### Day 1 – Multi-AZ VPC Architecture

- Designed a Multi-AZ VPC
- Configured public, application, and data subnet tiers
- Designed Internet Gateway and NAT Gateway architecture
- Created route tables and security groups
- Produced infrastructure diagrams in Draw.io

### Day 2 – Connectivity and Load Balancing

- Designed Application Load Balancer architecture
- Implemented path-based routing design
- Evaluated Transit Gateway, PrivateLink, and VPC Peering
- Designed Direct Connect hybrid architecture
- Completed connectivity decision workshop

### Day 3 – Route 53 and DNS

- Created Route 53 hosted zone architecture
- Configured Alias A records
- Configured CNAME records
- Implemented weighted routing design
- Designed canary deployment traffic flow
- Produced Route 53 architecture diagrams

---

## Key Concepts Demonstrated

### Networking

- VPC Design
- CIDR Planning
- Multi-AZ Architecture
- Internet Gateway
- NAT Gateway High Availability
- Route Tables
- Security Groups

### Connectivity

- AWS Transit Gateway
- VPC Peering
- AWS PrivateLink
- AWS Client VPN
- AWS Direct Connect

### Load Balancing

- Application Load Balancer (ALB)
- Layer 7 Routing
- Path-Based Routing
- Target Groups
- TLS Termination Concepts

### DNS and Route 53

- Hosted Zones
- Alias A Records
- CNAME Records
- Weighted Routing
- Failover Routing
- Latency Routing
- Geolocation Routing
- Canary Deployments

---

# Architecture Portfolio

## Week 05 Deliverables

### Multi-AZ VPC Architecture

Files:

```text
week05/fintrust-vpc.drawio
week05/fintrust-vpc.png
week05/day1_vpc_build.md
```

### ALB and Connectivity Design

Files:

```text
week05/day2_connectivity.md
```

### Route 53 DNS Architecture

Files:

```text
week05/route53.drawio
week05/route53.png
week05/day3_route53.md
```

---

# Architecture Context

All FinTrust artifacts form part of a 16-week cloud engineering project simulating a South African digital bank operating in the AWS Africa (Cape Town) Region (`af-south-1`).

Architecture decisions are documented weekly and are based on AWS Well-Architected Framework principles:

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability

---

# Progress Tracker

| Week | Theme | Status |
|--------|--------|--------|
| Week 1 | Foundation | ✅ Completed |
| Week 2 | Compute, SQL & Python Fundamentals | ✅ Completed |
| Week 3 | Python, Data Processing & Documentation | ✅ Completed |
| Week 4 | SQLite Reporting Pipeline | ✅ Completed |
| Week 5 | AWS Networking, Connectivity & DNS | ✅ Completed (Days 1–3) |
| Week 6 | Coming Soon | ⏳ Planned |
| Week 7 | Coming Soon | ⏳ Planned |
| Week 8 | Coming Soon | ⏳ Planned |
| Week 9 | Coming Soon | ⏳ Planned |
| Week 10 | Coming Soon | ⏳ Planned |
| Week 11 | Coming Soon | ⏳ Planned |
| Week 12 | Coming Soon | ⏳ Planned |
| Week 13 | Coming Soon | ⏳ Planned |
| Week 14 | Coming Soon | ⏳ Planned |
| Week 15 | Coming Soon | ⏳ Planned |
| Week 16 | Capstone & Certification Preparation | ⏳ Planned |

---

# Goal

Develop practical cloud engineering and solution architecture skills while preparing for the:

**AWS Certified Solutions Architect – Associate (SAA-C03)**

and building a portfolio that demonstrates real-world cloud architecture, automation, data engineering, networking, DNS, connectivity, and application development capabilities.