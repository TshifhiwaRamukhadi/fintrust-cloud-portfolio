FinTrust Cloud Portfolio

Learner: Tshifhiwa Ramukhadi
 Programme: Cloud to Solutions Accelerator (16 Weeks)
 Target Certification: AWS Certified Solutions Architect – Associate (SAA-C03)
 Cohort Start: 6 July 2026

About This Repository

This portfolio documents my work throughout the 16-week Cloud to Solutions Accelerator Programme.

Each weekly folder contains hands-on technical exercises, architecture decisions, SQL scripts, Python applications, cloud labs, and supporting documentation built around the FinTrust Bank case study.

The project simulates a South African digital banking environment deployed in the AWS Africa (Cape Town) Region (af-south-1), applying real-world cloud architecture, security, networking, data, and automation concepts.

Week 02: Compute, SQL Aggregates & Python Fundamentals
What I Built

SQL queries demonstrating:

INNER JOIN
LEFT JOIN
GROUP BY
HAVING

using the FinTrust Bank transactions dataset.

Python applications implementing a fraud detection decision engine using:

if / elif / else
Boolean logic
Membership testing with the in operator
Early return patterns
Decimal for currency accuracy
Key Concepts Demonstrated
AWS Compute Services

Amazon EC2

Persistent virtual servers
Suitable for long-running workloads

AWS Lambda

Event-driven serverless execution
Pay only when code runs

Amazon ECS

Container orchestration service
Ideal for microservices and containerized applications
Storage

gp3 EBS Volumes

General-purpose SSD storage
Cost-effective for most workloads

io2 EBS Volumes

High-performance SSD storage
Designed for mission-critical applications requiring sustained IOPS
SQL
Aggregate Functions
Joins
Data Grouping
Filtering with HAVING
Python
Conditional Logic
Boolean Expressions
Membership Operators
Currency Handling with Decimal
Fraud Detection Decision Flows
Project Structure
Plain Text
1
week02/
2
│
3
├── sql/
4
│ ├── joins_practice.sql
5
│ └── aggregates_report.sql
6
│
7
├── python/
8
│ ├── conditionals.py
9
│ └── transaction_flowchart.py
10
│
11
└── architecture/
12
└── week02_compute_notes.md
Show more lines
Files
File	Descriptionsql/joins_practice.sql	INNER JOIN and LEFT JOIN exercises
sql/aggregates_report.sql	Monthly transaction summaries using GROUP BY and HAVING
python/conditionals.py	Transaction classifier, interest-rate calculator, and ATM logic
python/transaction_flowchart.py	Fraud detection decision engine with five test scenarios
architecture/week02_compute_notes.md	Compute service selection and architecture decisions
How to Run
SQL Exercises

Requires SQLite:

Shell
1
sqlite3 :memory: ".read sql/joins_practice.sql"
2
sqlite3 :memory: ".read sql/aggregates_report.sql"
Show more lines
Python Exercises
Shell
1
python python/conditionals.py
2
python python/transaction_flowchart.py
3
``
Show more lines
Architecture Context

All FinTrust artifacts form part of a 16-week cloud engineering project simulating a South African digital bank operating in the AWS Africa (Cape Town) Region (af-south-1).

Architecture decisions are documented weekly and are based on AWS Well-Architected Framework principles, scalability requirements, operational excellence, security, performance efficiency, reliability, and cost optimization.

Progress Tracker
Week	Theme	StatusWeek 1	Foundation	✅ Completed
Week 2	Compute, SQL & Python Fundamentals	✅ Completed
Week 3	Coming Soon	⏳ Planned
Week 4	Coming Soon	⏳ Planned
Week 5	Coming Soon	⏳ Planned
Week 6	Coming Soon	⏳ Planned
Week 7	Coming Soon	⏳ Planned
Week 8	Coming Soon	⏳ Planned
Week 9	Coming Soon	⏳ Planned
Week 10	Coming Soon	⏳ Planned
Week 11	Coming Soon	⏳ Planned
Week 12	Coming Soon	⏳ Planned
Week 13	Coming Soon	⏳ Planned
Week 14	Coming Soon	⏳ Planned
Week 15	Coming Soon	⏳ Planned
Week 16	Capstone & Certification Preparation	⏳ Planned
Goal

Develop practical cloud engineering and solution architecture skills while preparing for the:

AWS Certified Solutions Architect – Associate (SAA-C03) certification and building a portfolio that demonstrates real-world cloud architecture, automation, data, and application development capabilities.