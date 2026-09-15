import pandas as pd
from io import StringIO
import os

csv_data = """transaction_id,account_id,amount,currency,timestamp,status
txn-001,ACC-0001,1500.00,ZAR,2024-06-01 09:15:33,COMPLETED
txn-002,ACC-0002,87000.00,ZAR,2024-06-01 09:22:11,COMPLETED
txn-003,ACC-0001,250.00,ZAR,2024-06-02 14:05:02,COMPLETED
txn-004,ACC-0003,12500.00,USD,2024-06-02 16:44:55,PENDING
"""

df = pd.read_csv(StringIO(csv_data))

# Transformations
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["year"] = df["timestamp"].dt.year.astype(str)
df["month"] = df["timestamp"].dt.month.astype(str).str.zfill(2)
df["is_high_value"] = df["amount"] > 50000

print(df.dtypes)
print(df.head())

# Partitioned Parquet output
for (year, month), group in df.groupby(["year", "month"]):

    path = (
        f"fintrust_processed/"
        f"year={year}/"
        f"month={month}/"
        f"transactions.parquet"
    )

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    group.drop(
        columns=["year", "month"]
    ).to_parquet(
        path,
        engine="pyarrow",
        index=False
    )

    print(
        f"Written: {path} "
        f"({len(group)} rows)"
    )