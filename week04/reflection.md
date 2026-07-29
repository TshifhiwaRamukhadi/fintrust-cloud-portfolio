# Week 4 Reflection

## What would break in this pipeline if two processes ran it at exactly the same time against the same SQLite file?

SQLite allows only limited concurrent write operations. If two pipeline processes attempted to write to the same database file simultaneously, one process could encounter database locking errors while waiting for the other transaction to complete. This can reduce reliability and throughput in multi-user environments.

## How would RDS Multi-AZ handle that differently?

Amazon RDS is designed for concurrent access by many users and applications. Multi-AZ deployments provide high availability by maintaining a synchronous standby database in another Availability Zone. If a database instance fails, RDS automatically performs failover while continuing to support concurrent connections and transactions.