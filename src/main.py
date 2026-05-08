"""
main.py
Main entry point of the CashTrack CLI application.
"""

from models import Transaction
from storage import load_transactions, save_transactions
from utils import (
    display_transactions,
    calculate_balance,
    search_transactions,
    sort_transactions,
)


def add_transaction(transactions):
    """Add a new transaction."""

    print("\n===== ADD TRANSACTION =====")

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: ₱"))

    except ValueError:
        print("Invalid amount input.")
        return

    transaction_type = input("Enter type (Income/Expense): ")
    description = input("Enter description: ")

    transaction = Transaction(
        category,
        amount,
        transaction_type,
        description,
    )

    transactions.append(transaction.to_dict())

    save_transactions(transactions)

    print("Transaction added successfully.\n")


def view_balance(transactions):
    """Display current balance."""

    balance = calculate_balance(transactions)

    print(f"\nCurrent Balance: ₱{balance}\n")


def search_menu(transactions):
    """Search transactions by category."""

    keyword = input("\nEnter category to search: ")

    results = search_transactions(transactions, keyword)

    display_transactions(results)


def sort_menu(transactions):
    """Display sorted transactions."""

    sorted_transactions = sort_transactions(transactions)

    print("\n===== SORTED TRANSACTIONS =====")

    display_transactions(sorted_transactions)


def main():
    """Run the CashTrack application."""

    transactions = load_transactions()

    while True:
        print("\nCASHTRACK")
        print("Student Expense Tracker\n")

        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Search Transactions")
        print("5. Sort Transactions")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_transaction(transactions)

        elif choice == "2":
            display_transactions(transactions)

        elif choice == "3":
            view_balance(transactions)

        elif choice == "4":
            search_menu(transactions)

        elif choice == "5":
            sort_menu(transactions)

        elif choice == "6":
            print("\nThank you for using CashTrack.")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()