# Week 6 Day 3: Introduction to boto3

## Objective

Learn how to use Python and boto3 to interact with AWS services.

## What is boto3?

boto3 is the AWS SDK for Python. It allows Python applications to communicate with AWS services.

Example:

```python
import boto3

s3 = boto3.client("s3")
```

## boto3 Client

A client provides direct access to AWS service APIs.

Example:

```python
s3 = boto3.client("s3")
```

## Common S3 Operations

List buckets:

```python
response = s3.list_buckets()
```

Get bucket location:

```python
s3.get_bucket_location(
    Bucket="bucket-name"
)
```

Get bucket encryption:

```python
s3.get_bucket_encryption(
    Bucket="bucket-name"
)
```

## Lab Activity

Build an S3 Audit Script that:

- Lists S3 buckets
- Checks the bucket region
- Checks public access settings
- Checks encryption status
- Produces a simple audit report

## Skills Demonstrated

- Python scripting
- boto3 usage
- AWS SDK interaction
- Exception handling
- Security auditing
``