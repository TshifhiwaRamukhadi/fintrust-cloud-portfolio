# Week 5 Mock Exam Review

## Score

Score:

__ / 15

Result:

- Excellent (13-15)
- Good (10-12)
- Needs Improvement (7-9)
- Revisit Week 5 Content (<7)

---

## Questions I Was Unsure About

List any questions where I guessed or was uncertain.

Example:

- Q2 – NACL stateless behavior
- Q7 – Alias vs CNAME
- Q10 – OAC configuration

---

## Review Notes

### NAT Gateway

Private instances requiring internet access should use a NAT Gateway located in a public subnet.

Key Exam Signal:

Outbound-only internet access for private instances.

Answer:

AWS NAT Gateway.

---

### Network ACLs

NACLs are stateless.

Return traffic requires explicit rules.

Example:

Inbound:

80 ALLOW

Outbound:

1024-65535 ALLOW

Missing ephemeral ports can break connectivity.

---

### Transit Gateway

Used when connecting multiple VPCs and on-premises environments.

Benefits:

- Centralized routing
- Hub-and-spoke architecture
- Transitive routing

Key Exam Signal:

Many VPCs + centralized routing.

---

### Application Load Balancer

Supports:

- Layer 7 routing
- Path-based routing
- Host-based routing
- HTTPS termination

Key Exam Signal:

/api/*
/portal/*
HTTPS
ACM

Answer:

ALB

---

### Network Load Balancer

Supports:

- TCP
- UDP
- Static IP addresses
- Very high performance

Key Exam Signal:

Static IP
TCP
Partner firewall allow lists

Answer:

NLB

---

### Route 53

#### Alias Record

Used for:

- Root domains
- AWS resources

Benefits:

- No fixed IP required
- Automatically updated

#### CNAME

Used only for subdomains.

Cannot be used at the zone apex.

---

### Route 53 Routing Policies

| Requirement | Policy |
|------------|---------|
| Route by country | Geolocation |
| Lowest RTT | Latency |
| Traffic percentage | Weighted |
| Disaster Recovery | Failover |
| Single endpoint | Simple |

---

### Route 53 Failover

Requirements:

- Failover routing record
- Health check

Without a health check, failover does not occur automatically.

---

### CloudFront

Benefits:

- Global content delivery
- Lower latency
- HTTPS support
- Edge caching

---

### OAC vs OAI

#### OAC

- Current AWS recommendation
- Supports KMS
- Better security
- Request signing

#### OAI

- Legacy solution
- Older access model

---

### CloudFront Invalidation

If cached content must update immediately:

Use:

CloudFront Invalidation

Example:

```text
/styles/main.css
```

This refreshes edge caches without waiting for TTL expiration.

---

### Direct Connect

Provides:

- Dedicated private connectivity
- Consistent latency
- No public internet

Recommended for enterprise hybrid architecture.

---

## Week 5 Learning Summary

This week covered:

- Multi-AZ VPC design
- NAT Gateway high availability
- Security Groups and NACLs
- Application Load Balancers
- Transit Gateway
- PrivateLink
- Direct Connect
- Route 53
- CloudFront
- Failover routing
- Weighted routing
- Secure S3 origins using OAC

The most important exam concepts were:

- NAT Gateway for private outbound access
- NACL stateless behavior
- ALB path-based routing
- Transit Gateway for many VPCs
- Alias records for root domains
- Route 53 Failover with health checks
- CloudFront OAC for private S3 access