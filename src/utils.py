"""
utils.py
Contains utility functions for displaying and processing transactions.
"""


def display_transactions(transactions):
    """Display all stored transactions."""

    if not transactions:
        print("\nNo transactions found.\n")
        return

    print("\n===== TRANSACTION LIST =====")

    for index, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction #{index}")
        print(f"Category: {transaction['category']}")
        print(f"Amount: ₱{transaction['amount']}")
        print(f"Type: {transaction['transaction_type']}")
        print(f"Description: {transaction['description']}")


def calculate_balance(transactions):
    """Calculate total balance from income and expenses."""

    income = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["transaction_type"].lower() == "income"
    )

    expense = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["transaction_type"].lower() == "expense"
    )

    return income - expense


def search_transactions(transactions, keyword):
    """Search transactions using category keyword."""

    results = [
        transaction
        for transaction in transactions
        if keyword.lower() in transaction["category"].lower()
    ]

    return results


def sort_transactions(transactions):
    """Sort transactions by amount."""

    return sorted(
        transactions,
        key=lambda transaction: transaction["amount"]
    )