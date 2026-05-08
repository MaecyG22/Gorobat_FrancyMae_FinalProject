"""
models.py
Defines the Transaction class used in CashTrack.
"""


class Transaction:
    """Represents a student's financial transaction."""

    def __init__(self, category, amount, transaction_type, description):
        """
        Initialize transaction details.

        Args:
            category (str): Transaction category.
            amount (float): Transaction amount.
            transaction_type (str): Income or Expense.
            description (str): Additional details.
        """

        self.category = category
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description

    def to_dict(self):
        """Convert transaction object into dictionary."""

        return {
            "category": self.category,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "description": self.description,
        }