# Week 5 Day 2 - ALB Path-Based Routing and Connectivity Design

## ALB Configuration

### Load Balancer

Name:

fintrust-alb

Type:

Application Load Balancer (ALB)

Scheme:

Internet-facing

VPC:

fintrust-vpc

Subnets:

- fintrust-public-1a
- fintrust-public-1b

Security Group:

- alb-sg

---

## Target Groups

### api-targets

Protocol: HTTP

Port: 8080

Health Check Path:

/api/health

Purpose:

Routes API traffic to backend transaction services.

### portal-targets

Protocol: HTTP

Port: 8080

Health Check Path:

/portal/health

Purpose:

Routes portal traffic to frontend services.

---

## Listener Configuration

Listener:

HTTP 80 (Lab)

Real-world deployment:

HTTPS 443 with ACM certificate

Default Action:

Forward to portal-targets

---

## Path-Based Routing Rules

### Rule 1

Condition:

/api/*

Action:

Forward to api-targets

### Rule 2

Condition:

/portal/*

Action:

Forward to portal-targets

### Default Rule

All unmatched requests are forwarded to portal-targets.

---

## Why ALB Instead of NLB?

Application Load Balancer operates at Layer 7 and understands HTTP and HTTPS traffic.

ALB supports:

- Path-based routing
- Host-based routing
- HTTP inspection
- TLS termination
- ECS and EKS integration

A Network Load Balancer operates at Layer 4 and cannot inspect URL paths. It would be unable to distinguish between /api/* and /portal/* requests.

---

# Connectivity Design Workshop

## Scenario 1

Requirement:

Connect fintrust-prod-vpc, fintrust-dev-vpc, and fintrust-audit-vpc with centralised routing and shared internet egress.

Answer:

AWS Transit Gateway

Justification:

Transit Gateway provides hub-and-spoke connectivity, centralized routing, and supports transitive routing between multiple VPCs.

---

## Scenario 2

Requirement:

Allow the audit VPC to privately access a third-party compliance reporting SaaS API without exposing FinTrust resources to the internet.

Answer:

AWS PrivateLink

Justification:

PrivateLink provides private service-level connectivity without requiring VPC peering, route table changes, or internet exposure.

---

## Scenario 3

Requirement:

Connect the on-premises mainframe to AWS with a dedicated private link, predictable latency, and no public internet.

Answer:

AWS Direct Connect

Justification:

Direct Connect provides a dedicated physical connection with predictable performance and consistent latency.

---

## Scenario 4

Requirement:

Allow 10 DevOps engineers to access the dev VPC remotely from their laptops.

Answer:

AWS Client VPN

Justification:

Client VPN is designed for individual user remote access into AWS environments.

---

# Why Not VPC Peering?

## Reason 1

VPC Peering does not support transitive routing.

For three VPCs:

- Prod ↔ Dev
- Prod ↔ Audit
- Dev ↔ Audit

must all be configured separately.

## Reason 2

VPC Peering becomes difficult to manage as environments grow.

Transit Gateway provides centralized management and scales better for multiple VPCs and accounts.

---

# Reflection

## Why does Direct Connect beat Site-to-Site VPN for FinTrust?

Direct Connect provides a dedicated private connection between the on-premises mainframe and AWS. It offers predictable latency, higher bandwidth, and does not depend on internet routing. Site-to-Site VPN uses the public internet and may experience variable latency and performance.

---

## Request Path Walkthrough

A user submits the following request:

/api/transfer

Traffic flow:

1. User browser sends HTTPS request.
2. DNS resolves the ALB endpoint.
3. Request reaches fintrust-alb in public subnets.
4. ALB evaluates listener rules.
5. Path matches /api/*.
6. ALB forwards traffic to api-targets.
7. ECS task handling transaction services processes the request.
8. Response returns through the ALB back to the user.

Flow:

User Browser
→ Route 53
→ ALB
→ api-targets
→ ECS Container
→ Response

---

## What happens to /payments/*?

No path rule exists for /payments/*.

The request follows the ALB default rule and is forwarded to portal-targets.

---

## Direct Connect vs Site-to-Site VPN

| Direct Connect | Site-to-Site VPN |
|---------------|------------------|
| Dedicated connection | Internet-based connection |
| Predictable latency | Variable latency |
| Higher bandwidth | Lower bandwidth |
| Better for enterprise workloads | Better for quick deployment |
| No reliance on public internet | Uses public internet |

---

## PrivateLink vs VPC Peering

### PrivateLink

Provides private access to a specific service.

Does not provide full VPC network connectivity.

### VPC Peering

Provides network-level connectivity between entire VPCs.

Resources in connected VPCs can communicate directly through private IP addresses.

---

## Key Takeaways

- ALB is required for path-based routing.
- NLB is used for TCP/UDP and static IP requirements.
- Transit Gateway enables scalable multi-VPC connectivity.
- PrivateLink provides private service access.
- Direct Connect provides dedicated hybrid connectivity.
- Client VPN is used for individual remote users.