# Week 9 Day 4: Migration Monitoring with Python

## Objective

Learn how to monitor migration activities using Python and boto3 by tracking AWS Database Migration Service (DMS) tasks, reviewing migration statistics, planning Snow Family transfers, and exploring AWS Fault Injection Simulator (FIS) monitoring.

---

## DMS Task Monitoring

AWS Database Migration Service (DMS) provides replication task monitoring capabilities through boto3.

The DMS monitoring process focuses on tracking migration progress, identifying errors, and validating successful data transfer between source and target systems.

Key monitoring operations include:

- describe_replication_tasks()
- describe_table_statistics()
- start_replication_task()
- stop_replication_task()

Monitoring task progress allows engineers to identify migration bottlenecks and track replication health throughout the migration lifecycle.

---

## DMS Task Status Lifecycle

A migration task progresses through a number of states:

### Creating

The replication task definition is being created and cannot yet be started.

### Ready

The task has been successfully configured and is ready for execution.

### Starting

DMS is establishing source and target connections and preparing replication.

### Running

Data is actively being migrated between the source and target environments.

### Stopped

The task was stopped manually or completed successfully.

### Failed

The migration task encountered an error and requires investigation.

### Deleting

The task is being removed from the environment.

---

## DMS Progress Monitoring

A monitoring utility was developed to retrieve migration progress information.

The utility reports:

- Task Identifier
- Replication Status
- Tables Loaded
- Tables Loading
- Tables Queued
- Tables Errored
- Full Load Progress Percentage
- Elapsed Runtime

This information gives migration teams visibility into replication performance and overall migration health.

---

## Change Data Capture (CDC)

FinTrust migrations use a two-stage approach:

### Full Load Phase

All existing records are copied from the source database to the target database.

### CDC Phase

After the full load completes, DMS continuously replicates:

- INSERT operations
- UPDATE operations
- DELETE operations

During CDC the replication task remains in a running state indefinitely while changes continue to flow from source to target.

For CDC workloads, monitoring should focus on:

- Table validation status
- Validation errors
- Full load error rows
- Table replication statistics

rather than FullLoadProgressPercent alone.

---

## Snow Family Transfer Planning

AWS Snow Family devices provide physical data transfer solutions for large migration workloads.

Available device options include:

### Snowcone

Small portable device suitable for edge and disconnected environments.

### Snowball Edge Storage Optimised

Large-scale storage migration platform providing approximately 80 TB of usable storage.

### Snowball Edge Compute Optimised

Provides storage alongside edge computing capabilities.

### Snowmobile

Designed for exabyte-scale migrations using a dedicated AWS transfer vehicle.

---

## FinTrust Archive Migration Scenario

FinTrust plans to migrate approximately:

```text
3 PB (3000 TB)