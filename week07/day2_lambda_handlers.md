# Week 7 Day 2 PM: Python in Lambda

## Objective

Learn how AWS Lambda executes Python functions and how event payloads, context objects and environment variables are used.

---

## Lambda Handler Anatomy

Every Lambda function requires:

```python
def lambda_handler(event, context):
```

### event

Contains the trigger payload.

Examples:

- API Gateway request
- SQS message
- S3 upload notification

### context

Contains runtime metadata.

Examples:

```python
context.function_name
context.aws_request_id
context.memory_limit_in_mb
context.function_version
```

---

## API Gateway Event

Example values:

```python
event["httpMethod"]
event["path"]
event["queryStringParameters"]
event["headers"]
event["body"]
```

Used when Lambda is invoked through HTTP endpoints.

---

## SQS Event

SQS delivers batches.

Example:

```python
event["Records"]
```

Each record contains:

```python
messageId
eventSourceARN
body
```

---

## S3 Event

Provides information about uploaded files.

Example:

```python
bucket_name =
record["s3"]["bucket"]["name"]

object_key =
record["s3"]["object"]["key"]
```

---

## Context Object

Useful information:

```python
context.function_name
context.function_version
context.aws_request_id
context.memory_limit_in_mb
```

The function can stop processing early if:

```python
context.get_remaining_time_in_millis()
```

shows insufficient remaining execution time.

---

## Environment Variables

Used to avoid hardcoding values.

Example:

```python
QUEUE_URL =
os.environ["PAYMENT_QUEUE_URL"]
```

Optional variable:

```python
ENVIRONMENT =
os.environ.get(
    "ENVIRONMENT",
    "dev"
)
```

---

## FinTrust Transaction Lambda

The function:

- Accepts transaction requests
- Reads account ID
- Reads transaction amount
- Validates input
- Returns an accepted response

Example request:

```json
{
  "body": "{\"account_id\":\"ACC-001\",\"amount\":500}"
}
```

Example response:

```json
{
  "status": "accepted",
  "account_id": "ACC-001"
}
```

---

## Reflection: Init vs Handler

Module-level initialization is executed only during Lambda cold starts.

Example:

```python
sqs = boto3.client("sqs")
```

This means AWS can reuse the execution environment and avoid recreating clients during every invocation.

If initialization were moved inside the handler, boto3 clients and configuration would be recreated every time the Lambda runs, increasing execution time and cost.