# Week 5 Day 1 - Multi-AZ VPC Lab

## VPC CIDR Table

fintrust-vpc          10.0.0.0/16

fintrust-public-1a    10.0.0.0/24
fintrust-public-1b    10.0.1.0/24

fintrust-app-1a       10.0.10.0/24
fintrust-app-1b       10.0.11.0/24

fintrust-data-1a      10.0.20.0/24
fintrust-data-1b      10.0.21.0/24

## Security Group Logic

alb-sg
- HTTPS 443 from 0.0.0.0/0

app-sg
- TCP 8080 from alb-sg

db-sg
- PostgreSQL 5432 from app-sg
- Redis 6379 from app-sg
- MongoDB 27017 from app-sg

## SG vs NACL Challenge

1. Block 41.0.0.0/8
Answer: NACL

2. Allow ALB to ECS on TCP 8080
Answer: Security Group

3. Database accepts traffic only from application tier
Answer: Security Group

## Traffic Path

Internet
→ Internet Gateway
→ Application Load Balancer
→ Application Tier
→ Database Tier

## Reflection

A public route table sends internet traffic through an Internet Gateway, allowing public access. A private route table sends internet traffic through a NAT Gateway, allowing outbound access only.

If NAT Gateway 1a fails, resources in app-1a and data-1a lose outbound internet access because their route table points to nat-1a.

The db-sg references app-sg rather than subnet CIDRs because Security Group references allow only approved application-tier resources to connect.

The most surprising thing about VPC networking was that creating an Internet Gateway alone does not provide internet access; the correct route table configuration is also required.