# Week 10 Day 1: Python Migration Scripts and SQL Views

## Objective

Build the FinTrust Migration Python package, create a reusable boto3 session factory, classify EC2 instances using migration tags, and introduce SQL Views as a reporting and migration management tool.

---

## Building the fintrust_migration Package

As migration programmes grow, managing dozens of standalone scripts becomes difficult. A Python package provides a centralised structure that allows migration engineers to share common functionality while maintaining consistency across all migration tools.

The FinTrust Migration package was designed to:

- Centralise boto3 session creation
- Reuse AWS client configuration
- Standardise migration helper functions
- Reduce duplicate code
- Simplify maintenance and testing

Package structure:

```text
fintrust_migration/
├── __init__.py
├── utils/
│   └── sessions.py
├── ec2/
│   └── classifier.py
├── rds/
├── s3/
```

---

## Centralised Session Factory

The session factory provides a single location for AWS authentication and configuration.

Benefits include:

- Consistent AWS region configuration
- Reduced credential management complexity
- Shared boto3 session reuse
- Improved maintainability

A Singleton pattern is used to ensure that only one boto3 session is created and reused throughout the package lifecycle.

---

## EC2 Migration Classification

FinTrust uses migration tags to classify workloads according to migration strategy and migration wave.

Supported migration strategies:

- Rehost
- Replatform
- Refactor
- Repurchase
- Retain
- Retire

The classifier reads the following tags:

```text
migration:strategy
migration:wave
```

and builds a migration portfolio summary.

This allows migration planners to quickly understand:

- Which workloads belong to each strategy
- Migration wave assignments
- Missing classifications
- Untagged resources requiring remediation

---

## Migration Portfolio Reporting

The classifier generates a portfolio summary showing:

- Total instances per strategy
- Percentage allocation
- Untagged resources
- Migration wave membership

Example output:

```text
REHOST        : 1254 instances
REPLATFORM    : 842 instances
REFACTOR      : 351 instances
REPURCHASE    : 148 instances
RETAIN        : 192 instances
RETIRE        : 60 instances
UNTAGGED      : 0 instances
```

This information helps migration teams track overall migration readiness.

---
## Classifier Validation

The classifier package was tested against the AWS training account using the boto3 EC2 API.

Result:

```text
Portfolio: {
    'replatform': [],
    'refactor': [],
    'repurchase': [],
    'retire': [],
    'retain': [],
    'rehost': []
}

Untagged: []
```

The classifier successfully connected to AWS and evaluated the EC2 inventory. No migration-tagged EC2 instances were present in the account at the time of testing, therefore no instances were assigned to migration strategies and no untagged instances were detected.

This confirms that:

- The fintrust_migration package imports correctly
- The session factory creates AWS clients successfully
- The EC2 classifier executes successfully
- AWS connectivity and authentication are functioning correctly
```

## SQL Views

A SQL View is a stored query that behaves like a virtual table.

Views do not store data directly. Instead, the underlying query executes whenever the view is accessed.

Benefits include:

- Simplified reporting
- Encapsulation of complex joins
- Security boundaries
- Stable APIs for dashboards
- Improved developer productivity

---

## Migration Status Reporting

Views allow migration stakeholders to retrieve migration status information without needing direct access to underlying source tables.

Example use cases include:

- QuickSight dashboards
- Migration progress reporting
- Executive status reporting
- Audit and compliance reporting

By placing logic in a view, changes to underlying database structures can often be implemented without impacting consumers.

---

## Wave Progress Reporting

Migration waves can be summarised through SQL Views that calculate:

- Total assets
- Completed assets
- In-progress assets
- Failed migrations
- Completion percentage

This provides a simple operational dashboard for migration tracking.

---

## Reflection

Building reusable Python packages promotes consistency, maintainability, and collaboration during large migration programmes. The fintrust_migration package centralises AWS connectivity and migration logic, making it easier for teams to develop and maintain migration tooling at scale. Combining API-driven automation with SQL reporting provides both operational visibility and management reporting capabilities. The EC2 classifier offers real-time insight into migration readiness, while SQL Views provide a stable reporting layer that can be consumed by dashboards, migration teams, and business stakeholders without exposing underlying database complexity.