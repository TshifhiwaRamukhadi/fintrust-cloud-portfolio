# Week 4 Reflection

## What would break in this pipeline if two processes ran it at exactly the same time against the same SQLite file?

SQLite supports limited concurrent writes. If two pipeline processes attempted to write to the same database file at the same time, one process could encounter a database lock while waiting for the other transaction to complete. This can lead to reduced throughput and temporary write failures.

## How would RDS Multi-AZ handle that differently?

Amazon RDS PostgreSQL supports concurrent connections from multiple users and applications. Multi-AZ deployments provide high availability through a standby database in another Availability Zone and automatic failover. This architecture is designed for production workloads with multiple concurrent transactions and greater resilience than a file-based SQLite database.