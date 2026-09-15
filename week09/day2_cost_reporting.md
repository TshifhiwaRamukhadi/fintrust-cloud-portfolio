# Week 9 Day 2 PM: Cost Explorer and Budgets Automation

## Objective

Build automated FinOps reporting solutions using:

- Cost Explorer API
- AWS Budgets API
- Amazon S3
- Python (boto3)

---

# Cost Explorer

The Cost Explorer service is global.

Client:

```python
ce = boto3.client(
    "ce",
    region_name="us-east-1"
)
```

Purpose:

- Monitor AWS spend
- Analyse trends
- Generate reports
- Support cost optimisation

---

# Cost Metrics

### Unblended Cost

Represents actual AWS charges.

Recommended for:

- Team showback
- Department reporting
- Cost ownership

### Blended Cost

Averages discounts across accounts in an AWS Organization.

Useful for:

- Consolidated billing reports

---

# Spend by Service Reporting

The report groups spend by:

```text
SERVICE
```

Examples:

- Amazon EC2
- Amazon S3
- Amazon RDS
- AWS Lambda

Benefits:

- Identify highest-cost services
- Focus optimisation efforts
- Support budget planning

---

# AWS Budgets

Purpose:

Monitor spending against targets.

Example:

```text
Budget: $15,000/month
Alert: 80%
```

Notifications allow teams to act before overspending occurs.

---

# FinTrust Budget Strategy

Analytics Team:

```text
Monthly Budget:
$15,000
```

Alert Threshold:

```text
80%
```

Purpose:

Prevent unexpected cost growth.

---

# Monthly Cost Report Pipeline

Workflow:

```text
Cost Explorer
      |
      v
Python Report Generator
      |
      v
Top 5 Services
      |
      v
S3 Report Storage
```

---

# Top Service Analysis

Calculate:

```text
Average spend
```

Across:

- Month 1
- Month 2
- Month 3

Then calculate:

```text
Month-over-month %
```

Formula:

```text
(Current - Previous)
--------------------
Previous
```

---

# S3 Report Storage

Report path:

```text
s3://fintrust-cost-reports/YYYY-MM/monthly_summary.txt
```

Benefits:

- Historical retention
- Easy retrieval
- Automated scheduling

---

# Reflection: Python vs QuickSight

Python reporting and QuickSight dashboards solve different business needs.

Python reports are ideal for automation. They can be scheduled, distributed automatically, uploaded to S3 and integrated into operational workflows without requiring user interaction. This makes Python suitable for compliance reporting, monthly executive summaries and recurring FinOps reporting.

QuickSight provides interactive visualisation, dashboard exploration, filtering and drill-down analysis. It is better suited to analysts investigating unexpected spending trends or comparing multiple business units interactively. QuickSight can also combine AWS cost data with business datasets and present results visually for decision makers.

At FinTrust, the Python pipeline would be used to automatically generate monthly cost reports for leadership, while QuickSight would be used during cost review meetings to investigate trends and optimisation opportunities in greater detail.