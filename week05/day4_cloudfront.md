# Week 5 Day 4 - CloudFront Distribution and Architecture Review

## Activity 176 Debrief - Route 53 Failover Routing

### Objective

Configure Route 53 Failover Routing to automatically redirect traffic to a secondary website when the primary website becomes unavailable.

---

## Failover Architecture

### Primary Endpoint

CafeInstance1

- Availability Zone 1
- Receives traffic during normal operation
- Monitored by a Route 53 health check

### Secondary Endpoint

CafeInstance2

- Availability Zone 2
- Serves as the failover target
- Receives traffic only when the primary endpoint becomes unavailable

---

## Health Check Configuration

Name:

Primary-Website-Health

Configuration:

- Endpoint Monitoring
- Fast Interval: 10 seconds
- Failure Threshold: 2
- CloudWatch Alarm Enabled
- SNS Email Notification Enabled

Purpose:

Route 53 continuously monitors the health of the primary web server and automatically triggers failover when the endpoint becomes unhealthy.

---

## Failover Timeline

### Normal Operation

User requests are routed to CafeInstance1.

```text
User
  |
  v
Route 53
  |
  v
Primary Website
```

### Failure Detected

- Health checks begin failing
- Route 53 records endpoint failures
- CloudWatch Alarm changes state
- SNS email notification is sent

### Failover

Route 53 marks the primary endpoint as unhealthy and starts returning the secondary DNS record.

```text
User
  |
  v
Route 53
  |
  v
Secondary Website
```

### Recovery

When the primary endpoint becomes healthy again, Route 53 can resume routing traffic to the primary endpoint.

---

## TTL Considerations

TTL (Time To Live) controls how long DNS results remain cached.

Example:

- TTL = 15 seconds (Lab)
- TTL = 60 seconds (Recommended for DR)

Lower TTL values:

- Faster failover
- Faster DNS updates

Higher TTL values:

- Slower failover
- Reduced DNS query volume

---

## CloudFront Distribution Configuration

### Objective

Secure access to FinTrust static website assets stored in Amazon S3.

---

## Origin Configuration

Origin:

fintrust-portal-assets

Type:

Amazon S3 Bucket

Access:

Private

Block Public Access:

ON

---

## CloudFront Settings

Viewer Protocol Policy:

Redirect HTTP to HTTPS

Default Root Object:

index.html

Origin Access:

Origin Access Control (OAC)

Compression:

Enabled

---

## Cache Behaviour

### Static Content

```text
/*
```

Cached through CloudFront edge locations.

### API Requests

```text
/api/*
```

Configuration:

Cache Policy:

CachingDisabled

Purpose:

Ensures dynamic API responses are not cached.

---

## Origin Access Control (OAC)

### What Is OAC?

Origin Access Control allows CloudFront to securely access objects stored in private S3 buckets.

CloudFront signs requests before accessing S3 resources.

---

## Why OAC Is Preferred

Benefits:

- Current AWS recommended solution
- Supports AWS KMS-encrypted buckets
- More secure request signing
- Better future compatibility
- Replaces Origin Access Identity (OAI)

---

## OAC vs OAI

| OAC | OAI |
|------|------|
| Modern solution | Legacy solution |
| AWS recommended | Being phased out |
| Supports KMS-encrypted buckets | Limited functionality |
| Stronger request signing | Older authentication model |
| Better future support | Legacy support only |

---

# FinTrust Week 5 Architecture Review

## DNS Layer

Services:

- Route 53 Hosted Zone
- Weighted Routing
- Failover Routing
- Health Checks

Purpose:

Provides DNS resolution, traffic management, and disaster recovery capabilities.

---

## CDN Layer

Services:

- CloudFront Distribution
- HTTPS Enforcement
- Origin Access Control

Purpose:

Improves performance, reduces latency, and protects S3 content from public access.

---

## Edge Layer

Service:

fintrust-alb

Routing Rules:

```text
/api/*
→ api-targets

/portal/*
→ portal-targets

Default
→ portal-targets
```

Purpose:

Provides Layer 7 path-based routing.

---

## VPC Layer

VPC:

fintrust-vpc

CIDR:

10.0.0.0/16

Availability Zones:

- af-south-1a
- af-south-1b

Subnets:

### Public

- Public Subnet 1a
- Public Subnet 1b

### Application

- App Subnet 1a
- App Subnet 1b

### Data

- Data Subnet 1a
- Data Subnet 1b

---

## NAT Layer

Services:

- NAT Gateway 1a
- NAT Gateway 1b

Purpose:

Provides highly available outbound internet access for private resources.

---

## Security Layer

Security Groups:

```text
alb-sg
   ↓
app-sg
   ↓
db-sg
```

Purpose:

Provides layered access control between application tiers.

---

## Storage Layer

Service:

fintrust-portal-assets

Configuration:

- Private S3 Bucket
- Block Public Access Enabled
- Accessible only through CloudFront OAC

---

## Connectivity Layer

Service:

AWS Transit Gateway

Connected Networks:

- Prod VPC
- Dev VPC
- Audit VPC

Purpose:

Provides centralized routing and scalable multi-VPC connectivity.

---

## Hybrid Connectivity

Service:

AWS Direct Connect

Connected Resource:

FinTrust On-Prem Mainframe

Purpose:

Provides dedicated private connectivity between AWS and on-premises environments.

---

# Reflection

## Why Is OAC Preferred Over OAI?

OAC is AWS's current recommended solution for securing S3 origins behind CloudFront. It supports modern security features, request signing, and AWS KMS encryption. OAI is the older approach and does not offer the same capabilities.

---

## When Would You Place CloudFront In Front Of An ALB?

CloudFront should be placed in front of an ALB when:

- Users are globally distributed
- Static content can be cached
- Reduced latency is required
- AWS WAF protection is needed
- HTTPS performance should be improved

Example:

Global customers accessing FinTrust APIs and customer portals.

---

## How Do You Immediately Deploy A CSS Fix When TTL Is 86400 Seconds?

Options:

1. Create a CloudFront Invalidation.
2. Upload the file with a new version number.
3. Reduce cache TTL values for future deployments.

The fastest method is to create a CloudFront invalidation so edge locations retrieve the latest content immediately.

---

## Week 5 Key Takeaways

- Route 53 Failover Routing requires a health check.
- Low TTL values improve disaster recovery response times.
- CloudFront improves performance and security.
- OAC is preferred over OAI.
- ALB provides Layer 7 path-based routing.
- NAT Gateways should be deployed per Availability Zone.
- Transit Gateway simplifies multi-VPC connectivity.
- Direct Connect supports enterprise hybrid architectures.
- Private S3 buckets should be accessed through CloudFront rather than directly from the internet.