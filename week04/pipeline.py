"""
FinTrust CSV-to-SQLite pipeline.

This pipeline reads transaction data from a CSV file, validates each record,
and loads valid transactions into a SQLite database using parameterised SQL.
The database is then queried to generate a daily operational dashboard report.
"""
