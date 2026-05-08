"""
storage.py
Handles loading and saving transaction data using JSON.
"""

import json

DATA_FILE = "data/data.json"


def load_transactions():
    """Load transactions from JSON file."""

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_transactions(transactions):
    """Save transactions to JSON file."""

    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)