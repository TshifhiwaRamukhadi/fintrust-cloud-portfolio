"""
FinTrust Bank — Transaction Processing Module
Week 4 Day 1 PM Lab
"""

from datetime import datetime


# ==================================================
# Exception Hierarchy
# ==================================================

class BankingError(Exception):
    """Root class for all FinTrust errors."""
    pass


class TransactionError(BankingError):
    """Base transaction error."""

    def __init__(self, txn_id, message):
        self.txn_id = txn_id
        super().__init__(f"[TXN:{txn_id}] {message}")


class InsufficientFundsError(TransactionError):
    """Raised when account balance is too low."""

    def __init__(self, txn_id, account_id, requested, available):
        self.account_id = account_id
        self.requested = requested
        self.available = available
        self.shortfall = requested - available

        super().__init__(
            txn_id,
            f"Short R{self.shortfall:.2f} on {account_id}"
        )


class AccountFrozenError(TransactionError):
    """Raised when account is frozen."""

    def __init__(self, txn_id, account_id, reason):
        self.account_id = account_id
        self.reason = reason

        super().__init__(
            txn_id,
            f"{account_id} frozen: {reason}"
        )


class InvalidAmountError(TransactionError):
    """Raised when amount is zero or negative."""

    def __init__(self, txn_id, amount):
        self.amount = amount

        super().__init__(
            txn_id,
            f"Invalid amount: R{amount:.2f}. Amount must be greater than zero."
        )


class DailyLimitExceededError(TransactionError):
    """Raised when a transaction exceeds daily limit."""

    def __init__(
        self,
        txn_id,
        account_id,
        limit,
        already_used,
        requested
    ):
        self.account_id = account_id
        self.limit = limit
        self.already_used = already_used
        self.requested = requested

        remaining = limit - already_used

        super().__init__(
            txn_id,
            f"Daily limit R{limit:.2f}. "
            f"Used R{already_used:.2f}, "
            f"remaining R{remaining:.2f}, "
            f"requested R{requested:.2f}"
        )


# ==================================================
# Simple Account Store
# ==================================================

ACCOUNTS = {
    "FT-001234": {
        "balance": 3200.50,
        "frozen": False,
        "daily_used": 0.0,
        "daily_limit": 10000.0
    },

    "FT-005678": {
        "balance": 50000.00,
        "frozen": True,
        "daily_used": 0.0,
        "daily_limit": 50000.0,
        "freeze_reason": "POPIA compliance hold"
    },

    "FT-009999": {
        "balance": 1500.00,
        "frozen": False,
        "daily_used": 8500.0,
        "daily_limit": 10000.0
    },
}


# ==================================================
# Transaction Processor
# ==================================================

def process_withdrawal(txn_id: str, account_id: str, amount: float) -> dict:
    """
    Process a withdrawal.

    Returns:
        dict on success

    Raises:
        TransactionError subclasses on failure
    """

    # Validate amount
    if amount <= 0:
        raise InvalidAmountError(txn_id, amount)

    # Check account exists
    if account_id not in ACCOUNTS:
        raise TransactionError(
            txn_id,
            f"Account {account_id} not found"
        )

    account = ACCOUNTS[account_id]

    # Check frozen account
    if account["frozen"]:
        raise AccountFrozenError(
            txn_id,
            account_id,
            account.get("freeze_reason", "Unknown reason")
        )

    # Check daily limit
    if account["daily_used"] + amount > account["daily_limit"]:
        raise DailyLimitExceededError(
            txn_id,
            account_id,
            account["daily_limit"],
            account["daily_used"],
            amount
        )

    # Check balance
    if amount > account["balance"]:
        raise InsufficientFundsError(
            txn_id,
            account_id,
            amount,
            account["balance"]
        )

    # Process withdrawal
    account["balance"] -= amount
    account["daily_used"] += amount

    return {
        "txn_id": txn_id,
        "account_id": account_id,
        "amount": amount,
        "new_balance": account["balance"],
        "timestamp": datetime.now().isoformat(),
        "status": "SUCCESS"
    }


# ==================================================
# Main Test Harness
# ==================================================

if __name__ == "__main__":

    test_cases = [
        ("TXN001", "FT-001234", 100.00),      # success
        ("TXN002", "FT-001234", 5000.00),     # insufficient funds
        ("TXN003", "FT-005678", 500.00),      # frozen
        ("TXN004", "FT-009999", 2000.00),     # daily limit
        ("TXN005", "FT-001234", -50.00),      # invalid amount
    ]

    for txn_id, account_id, amount in test_cases:

        try:
            result = process_withdrawal(
                txn_id,
                account_id,
                amount
            )

            print(
                f"✓ {txn_id}: SUCCESS — "
                f"new balance R{result['new_balance']:.2f}"
            )

        except InsufficientFundsError as e:
            print(
                f"✗ {txn_id}: INSUFFICIENT FUNDS — "
                f"{e} (shortfall: R{e.shortfall:.2f})"
            )

        except AccountFrozenError as e:
            print(
                f"✗ {txn_id}: ACCOUNT FROZEN — {e}"
            )

        except DailyLimitExceededError as e:
            print(
                f"✗ {txn_id}: DAILY LIMIT EXCEEDED — {e}"
            )

        except InvalidAmountError as e:
            print(
                f"✗ {txn_id}: INVALID AMOUNT — {e}"
            )

        except TransactionError as e:
            print(
                f"✗ {txn_id}: TRANSACTION ERROR — {e}"
            )

        except BankingError as e:
            print(
                f"✗ {txn_id}: BANKING ERROR — {e}"
            )