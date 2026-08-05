# Week 5 Day 3 - Route 53 Hosted Zone Lab and Routing Policies

## Hosted Zone Configuration

### Hosted Zone

Domain Name:

fintrust-lab.internal

Type:

Public Hosted Zone (Lab Environment)

Automatically Created Records:

- NS (Name Server) Records
- SOA (Start of Authority) Record

Purpose:

Provides DNS management for FinTrust applications and services.

---

## Alias A Record

Record Name:

app

Fully Qualified Domain Name:

app.fintrust-lab.internal

Record Type:

A Record (Alias)

Target:

fintrust-alb

Purpose:

Routes application traffic directly to the Application Load Balancer.

### Why Alias Records?

Alias records:

- Support root domains
- Automatically track AWS resource changes
- Are free for AWS resources
- Do not require fixed IP addresses

---

## CNAME Record

Record Name:

api

Fully Qualified Domain Name:

api.fintrust-lab.internal

Record Type:

CNAME

Value:

fintrust-alb DNS Name

Example:

fintrust-alb-123456.af-south-1.elb.amazonaws.com

TTL:

300 seconds

Purpose:

Routes API traffic to the same ALB through a DNS alias.

### Important Limitation

CNAME records cannot be created at the zone apex (root domain).

Example:

✅ api.fintrust-lab.internal

❌ fintrust-lab.internal

For root domains, use an Alias A Record instead.

---

## Weighted Routing Configuration

### Production Record

Record Name:

canary.fintrust-lab.internal

Routing Policy:

Weighted

Record ID:

production

Weight:

90

Target:

fintrust-alb

Purpose:

Receives approximately 90% of production traffic.

---

### Canary Record

Record Name:

canary.fintrust-lab.internal

Routing Policy:

Weighted

Record ID:

canary

Weight:

10

Target:

Secondary ALB (or same ALB for lab simulation)

Purpose:

Receives approximately 10% of user traffic for testing new application versions.

---

## Canary Deployment Strategy

A canary deployment gradually introduces a new application version to a small percentage of users before a full rollout.

Example rollout process:

### Phase 1

Production: 100

Canary: 0

### Phase 2

Production: 90

Canary: 10

### Phase 3

Production: 50

Canary: 50

### Phase 4

Production: 0

Canary: 100

Benefits:

- Reduced deployment risk
- Easier problem detection
- Safer production releases
- Quick rollback if issues are identified

---

# Routing Policy Decision Quiz

## Scenario 1

Requirement:

Route customers in Nigeria to Lagos and customers in South Africa to Cape Town.

Answer:

Geolocation Routing

Reason:

Traffic is routed based on the user's geographic location.

---

## Scenario 2

Requirement:

Send 80% of traffic to production and 20% to a new application version.

Answer:

Weighted Routing

Reason:

Weighted routing distributes traffic according to percentages.

---

## Scenario 3

Requirement:

Route requests to the server with the lowest latency.

Answer:

Latency Routing

Reason:

Route 53 selects the endpoint with the lowest round-trip time.

---

## Scenario 4

Requirement:

If the primary ALB fails, automatically route traffic to a standby ALB.

Answer:

Failover Routing

Reason:

Failover routing uses health checks to switch traffic when the primary target becomes unavailable.

---

## Scenario 5

Requirement:

Spread traffic equally across three ALBs.

Answer:

Weighted Routing (equal weights)

Reason:

Traffic is distributed evenly among all endpoints.

---

## Scenario 6

Requirement:

Route all traffic to a single endpoint with no health checks or routing logic.

Answer:

Simple Routing

Reason:

Only a single record is required.

---

# Reflection

## What is TTL Propagation Delay and Why Does It Matter?

TTL (Time To Live) determines how long DNS resolvers cache a DNS response.

A higher TTL reduces DNS query traffic but causes slower propagation when DNS records change.

A lower TTL allows faster failover and quicker updates but increases DNS lookups.

For failover configurations, a TTL of approximately 60 seconds is often preferred.

---

## How Would You Gradually Roll Out a New Version Using Weighted Routing?

Weighted routing allows traffic to be shifted gradually from the production environment to the new version.

Example rollout:

- 100% / 0%
- 90% / 10%
- 50% / 50%
- 0% / 100%

This enables testing under production conditions while limiting risk.

---

## In What Scenario Would Geoproximity Routing Be Better Than Geolocation Routing?

Geolocation routing makes decisions based on country or continent boundaries.

Geoproximity routing routes users based on the physical distance from AWS Regions or resources.

Geoproximity is better when users should be directed to the nearest available region regardless of country borders.

Example:

A user located near the border between two countries may achieve better performance when routed to the closest AWS Region rather than a region selected solely by country.

---

## Can Route 53 Replace a Load Balancer?

No.

Route 53 is a DNS service that determines where requests should be sent.

Load balancers process and distribute live traffic between targets.

Route 53:

- DNS resolution
- Health-check based routing
- Traffic steering
- Regional selection

Application Load Balancer:

- Terminates HTTPS
- Performs path-based routing
- Performs host-based routing
- Balances traffic across targets
- Integrates with ECS and EKS

The two services complement each other rather than replace each other.

---

## Difference Between Latency Routing and Geolocation Routing

### Geolocation Routing

Routes traffic according to a user's country, continent, or geographic region.

Example:

- South Africa → Cape Town
- Nigeria → Lagos

### Latency Routing

Routes traffic to the endpoint with the lowest measured latency.

A South African user may be routed to a region outside South Africa if it delivers lower latency.

Geolocation is location-based.

Latency routing is performance-based.

---

## Key Route 53 Exam Signals

| Requirement | Routing Policy |
|------------|---------------|
| Route by country | Geolocation |
| Route by lowest latency | Latency |
| Canary deployment | Weighted |
| Active/Passive failover | Failover |
| Single endpoint | Simple |
| Equal traffic across endpoints | Weighted (equal weights) |

---

## FinTrust DNS Architecture

### Hosted Zone

fintrust-lab.internal

### Records

app → Alias A → fintrust-alb

api → CNAME → fintrust-alb DNS name

canary → Weighted Routing

- Production: 90%
- Canary: 10%

### Design Principles

- Alias records for AWS resources
- CNAME for subdomains
- Weighted routing for canary deployments
- Low TTL values for failover scenarios
- Health checks for availability monitoring

---

## Key Takeaways

- Alias records are preferred for AWS resources.
- CNAME records cannot be used at the root domain.
- Weighted routing enables canary deployments.
- Failover routing supports disaster recovery.
- Geolocation routing uses user location.
- Latency routing uses network performance.
- Route 53 works with load balancers rather than replacing them.