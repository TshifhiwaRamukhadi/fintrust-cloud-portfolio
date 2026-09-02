# Week 6 Day 4: Python Security Automation

## Objective

Automate AWS security checks using boto3.

## Scripts Built

### IAM MFA Audit

Checks IAM users with console access and identifies users who do not have MFA configured.

### Security Group Audit

Detects Security Groups that expose restricted ports to the internet:

- SSH (22)
- RDP (3389)
- PostgreSQL (5432)
- MySQL (3306)
- Oracle (1521)

### Stale Access Key Audit

Identifies IAM access keys older than 90 days.

### Report Generation

Combines findings into a JSON document and uploads it to S3.

## Reflection

Two ways to automate the audit:

### Option 1

Schedule an AWS Lambda function using EventBridge every Monday morning.

### Option 2

Run the script from an EC2 instance using a cron job or Task Scheduler.

### Preferred Approach

Lambda with EventBridge is more resilient because there are no servers to maintain, it scales automatically, and AWS manages availability.