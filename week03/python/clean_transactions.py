"""
clean_transactions.py
Reads raw FinTrust transaction CSV, cleans it,
outputs clean CSV + JSON summary.
"""

import csv
import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent

RAW_INPUT = BASE_DIR / "data" / "raw_transactions.csv"
CLEAN_CSV = BASE_DIR / "data" / "clean_transactions.csv"
SUMMARY_JSON = BASE_DIR / "data" / "daily_summary.json"


def normalise_date(date_str):
    """Convert dates into YYYY-MM-DD format."""

    formats = [
        "%Y-%m-%d",
        "%d/%m/%y",
        "%d/%m/%Y"
    ]

    for fmt in formats:
        try:
            return datetime.strptime(
                date_str.strip(),
                fmt
            ).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return date_str.strip()


def clean_transaction(row):
    """Clean a single transaction record."""

    return {
        "transaction_id": int(row["TxID"].strip()),
        "account_id": int(row["AcctID"].strip()),
        "type": row["TYPE"].strip().lower(),
        "amount": float(row["Amount"].strip()),
        "date": normalise_date(row["Date"]),
        "description": row["Desc"].strip() or "No description"
    }


def build_summary(transactions):
    """Build summary statistics."""

    deposits = [
        t for t in transactions
        if t["type"] == "deposit"
    ]

    withdrawals = [
        t for t in transactions
        if t["type"] == "withdrawal"
    ]

    return {
        "total_transactions": len(transactions),
        "total_deposits": len(deposits),
        "total_withdrawals": len(withdrawals),
        "sum_deposits": round(
            sum(t["amount"] for t in deposits),
            2
        ),
        "sum_withdrawals": round(
            sum(t["amount"] for t in withdrawals),
            2
        ),
    }


def main():

    transactions = []

    with open(
        RAW_INPUT,
        "r",
        newline="",
        encoding="utf-8"
    ) as fin:

        reader = csv.DictReader(fin)

        for row in reader:
            try:
                transactions.append(
                    clean_transaction(row)
                )
            except (ValueError, KeyError) as error:
                print(f"Skipped row: {error}")

    CLEAN_CSV.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "transaction_id",
        "account_id",
        "type",
        "amount",
        "date",
        "description"
    ]

    with open(
        CLEAN_CSV,
        "w",
        newline="",
        encoding="utf-8"
    ) as fout:

        writer = csv.DictWriter(
            fout,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(transactions)

    summary = build_summary(transactions)

    with open(
        SUMMARY_JSON,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            summary,
            f,
            indent=2
        )

    print(f"Clean CSV created: {CLEAN_CSV}")
    print(f"Summary JSON created: {SUMMARY_JSON}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()