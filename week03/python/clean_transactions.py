import csv
import json
from pathlib import Path


INPUT_FILE = Path("sample_transactions.csv")
OUTPUT_FILE = Path("cleaned_transactions.csv")
SUMMARY_FILE = Path("transaction_summary.json")


def clean_transactions():
    cleaned_rows = []

    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["customer_name"] = row["customer_name"].strip().title()
            row["amount"] = float(row["amount"])

            cleaned_rows.append(row)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=cleaned_rows[0].keys()
        )

        writer.writeheader()
        writer.writerows(cleaned_rows)

    total_transactions = len(cleaned_rows)
    total_amount = sum(row["amount"] for row in cleaned_rows)

    summary = {
        "total_transactions": total_transactions,
        "total_amount": total_amount
    }

    with open(SUMMARY_FILE, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print("Transaction cleaning complete.")
    print(f"Records processed: {total_transactions}")
    print(f"Summary written to: {SUMMARY_FILE}")


if __name__ == "__main__":
    clean_transactions()