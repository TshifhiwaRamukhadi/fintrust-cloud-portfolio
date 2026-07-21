# Week 2 Day 4
# Python Conditional Exercises

def classify_transaction(amount):
    if 0 < amount <= 100:
        return "MICRO"
    elif amount <= 1000:
        return "SMALL"
    elif amount <= 10000:
        return "STANDARD"
    elif amount > 10000:
        return "LARGE"
    else:
        return "INVALID"


def get_interest_rate(credit_score):
    if credit_score >= 750:
        return 7.5
    elif credit_score >= 700:
        return 9.5
    elif credit_score >= 650:
        return 12.0
    else:
        return 18.5


def atm_withdraw(balance, amount):
    if amount <= 0:
        return (False, "Invalid amount")
    elif amount > 5000:
        return (False, "ATM daily limit is R5 000")
    elif amount > balance:
        return (False, "Insufficient funds")
    else:
        return (True, f"Dispensing R{amount:.2f}")


def tag_transaction(tx_type, merchant_category, amount):
    if tx_type == "REFUND":
        return "REFUND"
    elif merchant_category == "GAMBLING":
        return "HIGH_RISK"
    elif merchant_category == "GROCERY" and amount < 500:
        return "ROUTINE"
    elif amount > 10000:
        return "LARGE_PURCHASE"
    else:
        return "STANDARD"


# Tests
print(classify_transaction(50))
print(get_interest_rate(720))
print(atm_withdraw(3000, 1500))
print(tag_transaction("DEBIT", "GROCERY", 200))