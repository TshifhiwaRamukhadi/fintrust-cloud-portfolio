# Week 9 Day 1 PM: AWS Cost Estimation with Python

## Objective

Use the AWS Pricing API and Python to build financial models that support cloud migration decisions and cost optimisation.

---

# AWS Pricing API

The AWS Pricing service is global.

Client configuration:

```python
pricing = boto3.client(
    "pricing",
    region_name="us-east-1"
)
```

Important:

The pricing API always uses:

```text
us-east-1
```

regardless of where workloads run.

---

# Pricing API Operations

## get_products()

Used to retrieve:

- EC2 prices
- Storage pricing
- Managed service pricing

## describe_services()

Used to discover:

- Available services
- Pricing attributes
- Filter names

---

# EC2 On-Demand Pricing

Example filters:

- Instance type
- Region
- Operating system
- Tenancy
- Capacity status

Example:

```python
get_ec2_ondemand_price(
    "m5.xlarge",
    "af-south-1"
)
```

Returns:

```text
Hourly USD price
```

---

# 730 Hour Rule

AWS commonly estimates monthly cost using:

```text
730 hours
```

Formula:

```text
Monthly cost =
Hourly cost × 730
```

---

# Savings Plans

Savings Plans provide reduced pricing in exchange for a long-term usage commitment.

## Compute Savings Plan

Benefits:

- Flexible
- Covers EC2
- Covers Lambda
- Covers Fargate

Discount:

```text
Up to 66%
```

---

## EC2 Instance Savings Plan

Benefits:

- Higher discounts

Trade-off:

- Less flexibility

Discount:

```text
Up to 72%
```

---

# FinTrust Savings Plan Scenario

Commitment:

```text
$32.47/hr
```

Term:

```text
3 Years
```

Result:

```text
~$847,000 savings
```

compared to On-Demand pricing.

---

# TCO Analysis

Inputs:

| Metric | Value |
|----------|----------|
| On-prem annual cost | $4,200,000 |
| AWS monthly cost | $248,000 |
| Migration cost | $850,000 |
| Inflation | 3% |

Purpose:

Identify when AWS becomes cheaper than continuing on-premises operations.

---

# Cost Optimisation Principles

## On-Demand

Best for:

- Short-term workloads
- Variable demand

## Savings Plans

Best for:

- Predictable workloads
- Long-term usage

## Spot Instances

Best for:

- Batch jobs
- Analytics
- EMR task nodes

---

# Reflection: TCO Limitations

A TCO model provides valuable insight into infrastructure costs, licensing expenses and operational spending. However, it cannot measure migration risk, organisational change management effort, application modernisation complexity or business disruption during migration activities.

The most important caveat when presenting a TCO model to FinTrust executives is that break-even calculations represent financial projections rather than guaranteed outcomes. Actual results depend on workload utilisation, migration success, operational efficiency and future business requirements. Cost should therefore be considered alongside risk, agility, compliance and strategic business value.