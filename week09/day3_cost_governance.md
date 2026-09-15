# Week 9 Day 3 PM: Cost Governance Automation

## Objective

Automate governance controls using:

- Resource Groups Tagging API
- AWS Service Catalog
- Amazon S3
- Python (boto3)

---

# Resource Groups Tagging API

Client:

```python
tagging = boto3.client(
    "resourcegroupstaggingapi",
    region_name="af-south-1"
)
```

Purpose:

- Discover resources
- Audit compliance
- Apply tags
- Remove tags

---

# FinTrust Tagging Standards

Required Tags:

```text
CostCentre
Team
Environment
```

Additional Tag:

```text
MigrationPhase
```

Used for migration tracking.

---

# CostCentre Values

```text
CoreBanking
Analytics
Security
DevOps
Migration
```

Purpose:

Support chargeback and showback reporting.

---

# Team Values

```text
Platform
DataEngineering
AppSec
SRE
DataMigration
```

Purpose:

Allocate spend to responsible teams.

---

# Environment Values

```text
Production
Staging
Dev
Sandbox
```

Purpose:

Separate operational and financial reporting.

---

# Compliance Audit Workflow

```text
AWS Resources
       |
       v
Tagging API
       |
       v
Compliance Scanner
       |
       v
Violation Report
```

---

# Auto Remediation Process

Workflow:

```text
Missing Environment Tag
         |
         v
Auto Apply:
Environment=Production
         |
         v
Re-run Audit
```

Purpose:

Reduce governance violations.

Note:

FinTrust generally prefers reporting and manual correction before applying automatic remediation.

---

# Service Catalog

Purpose:

Provide approved infrastructure products.

Benefits:

- Consistent deployments
- Enforced governance
- Approved architectures
- Mandatory tagging

---

# Service Catalog Workflow

```text
Developer
      |
      v
Service Catalog Product
      |
      v
CloudFormation
      |
      v
AWS Resources
```

Developers never interact directly with production templates.

---

# Governance Report Output

JSON Summary:

```json
{
  "total_scanned": 120,
  "initial_violations": 18,
  "auto_remediated": 14,
  "remaining_violations": 4
}
```

Storage Location:

```text
s3://fintrust-governance/tag-audit/YYYY-MM-DD.json
```

---

# Detect vs Enforce

Tagging API is a detective control.

It identifies problems after deployment.

Service Catalog is a preventive control.

It enforces tagging during deployment.

Neither control guarantees that tag values are correct.

A resource might contain:

```text
Environment=Prod123
```

instead of:

```text
Environment=Production
```

and still pass a simple tag existence audit.

To close this governance gap, FinTrust should implement:

## AWS Config

Benefits:

- Continuous compliance monitoring
- Custom compliance rules
- Approved value enforcement
- Automatic remediation actions

Example:

```text
Environment must be:
Production
Staging
Dev
Sandbox
```

AWS Config can continuously evaluate resources and flag incorrect values immediately.

---

# Reflection

Resource tagging is foundational to FinOps because Cost Explorer, Budgets, CUR reports and chargeback models depend on accurate metadata. Detecting missing tags is important, but preventing non-compliant resources from being created and validating tag values through AWS Config provides stronger governance. Combining Service Catalog, AWS Config and the Tagging API gives FinTrust preventive, detective and corrective governance controls across all AWS accounts.