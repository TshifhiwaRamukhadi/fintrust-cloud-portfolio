# Week 10 Architecture Narrative

## Migration Strategy Selection

The FinTrust migration programme uses a combination of migration approaches based on application complexity, business requirements, and migration risk.

Applications requiring minimal modification are classified as Rehost candidates and can be migrated quickly using infrastructure replication and lift-and-shift techniques.

Applications requiring platform improvements are classified as Replatform candidates, while highly strategic business systems are considered for Refactor where cloud-native capabilities provide long-term benefits.

Legacy applications with limited business value are evaluated for Retire or Retain strategies.

## DMS and DataSync Usage

AWS Database Migration Service (DMS) is used for database migration and ongoing Change Data Capture (CDC). DMS enables near-zero downtime migrations by continuously replicating database changes until cutover.

AWS DataSync is used for large-scale file transfers and NAS migrations. DataSync provides automated scheduling, verification, bandwidth throttling, and encrypted transfer capabilities.

## Automation Approach

The fintrust_migration package centralises migration operations into reusable Python modules.

The package provides:

- EC2 workload classification
- Migration wave identification
- DMS task management
- CDC lag monitoring
- DataSync transfer automation
- Dynamic bandwidth throttling
- Migration reporting support

This approach reduces manual effort, improves consistency, and supports repeatable migration processes.

## Benefits

The automated workflow improves migration visibility, reduces operational risk, and allows engineers to focus on migration planning and validation activities rather than repetitive monitoring tasks.

The combination of Python automation and SQL reporting provides both operational controls and business reporting capabilities throughout the migration lifecycle.

# Reflection

The fintrust_migration package demonstrates how migration operations can be automated using Python and AWS services. The package currently supports workload classification, DMS monitoring, DataSync execution management, bandwidth throttling, and migration reporting.

As the programme moves into governance and monitoring topics, I would extend the package with a new governance module.

Proposed module:

```text
fintrust_migration/
└── governance/
    ├── organizations.py
    ├── config_rules.py
    └── cloudtrail_audit.py
```

The governance module would automate:

- AWS Organizations account inventory
- Service Control Policy monitoring
- AWS Config compliance reporting
- CloudTrail audit analysis
- Security findings reporting

I would also add monitoring capabilities using CloudWatch dashboards and automated alerts to provide operational visibility across the migration environment.

This would transform the package from a migration execution toolkit into a broader migration governance and operational management platform.