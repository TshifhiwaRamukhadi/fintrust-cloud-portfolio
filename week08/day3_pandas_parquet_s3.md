# Week 8 Day 3 PM: Data Engineering with Pandas, Parquet and S3

## Objective

Process FinTrust transaction data using:

- Pandas
- PyArrow
- Parquet
- Amazon S3

---

## CSV vs Parquet

### CSV

Characteristics:

- Row-based format
- No embedded schema
- Limited compression
- Higher Athena scan costs

### Parquet

Characteristics:

- Columnar storage
- Embedded schema
- High compression
- Faster Athena queries
- Lower query cost

---

## Why Parquet Matters

Athena pricing is based on the amount of data scanned.

Parquet allows Athena to read only the required columns rather than scanning the entire dataset.

Benefits:

- Lower cost
- Faster performance
- Better scalability

---

## ETL Process

### Extract

Read transaction data from CSV.

```python
pd.read_csv(...)
```

### Transform

Performed transformations:

- Parse timestamp
- Create year partition
- Create month partition
- Flag high-value transactions

```python
is_high_value = amount > 50000
```

### Load

Write partitioned Parquet files:

```text
year=2024/
month=06/
transactions.parquet
```

---

## Hive Partition Structure

Example:

```text
s3://fintrust-processed/
transactions/
year=2024/
month=06/
transactions.parquet
```

Benefits:

- Partition pruning
- Faster queries
- Reduced Athena scanning costs

---

## Upload to S3

Used:

```python
boto3.client("s3")
```

Uploaded Parquet partitions while preserving:

```text
year=
month=
```

folder structure.

---

## Data Analysis

### High-Value Transactions

Criteria:

```text
amount > 50000
```

Used to identify potentially suspicious activity.

### Currency Summary

Calculated total transaction amounts by currency.

Example:

```python
df.groupby("currency")
```

---

## Reflection: Pandas vs Athena

### Pandas

I would use Pandas for local analysis, data exploration, machine learning preparation and ETL development where the dataset is small enough to fit into memory. Pandas gives data engineers and data scientists maximum flexibility for manipulating data programmatically.

### Athena

I would use Athena when working with large volumes of transaction data stored in S3. Athena is ideal for production reporting and compliance queries because it scales automatically, uses SQL that is familiar to analysts, and avoids loading large datasets into a local machine.