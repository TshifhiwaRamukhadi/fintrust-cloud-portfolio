# Week 6 Day 3 - Introduction to Python and boto3

## Objective

Learn how to automate AWS tasks using Python and boto3.

boto3 is AWS's official Python SDK and allows Python scripts to interact with AWS services programmatically.

---

## What is boto3?

boto3 is the AWS SDK for Python.

Common use cases:

- List S3 buckets
- Describe EC2 instances
- Manage IAM users
- Access DynamoDB tables
- Automate AWS operations

---

## Authentication Methods

boto3 searches for credentials in the following order:

1. Environment Variables
2. ~/.aws/credentials
3. IAM Role (EC2)
4. Task Role (ECS/Lambda)

Best Practice:

Never hardcode AWS credentials.

Use IAM Roles whenever possible.

---

## Client vs Resource

### Client

Low-level AWS API interface.

Returns raw JSON responses.

Example:

```python
s3 = boto3.client('s3')

## Script Execution Result

The boto3 package was successfully installed and the S3 audit script executed.

The script reached the AWS API call stage but returned:

```text
botocore.exceptions.NoCredentialsError:
Unable to locate credentials