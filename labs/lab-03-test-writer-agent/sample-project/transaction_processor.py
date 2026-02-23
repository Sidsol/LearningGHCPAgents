from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum
from typing import Optional
import uuid


class TransactionType(Enum):
    DEBIT = "debit"
    CREDIT = "credit"
    TRANSFER = "transfer"


@dataclass
class Transaction:
    amount: float
    transaction_type: TransactionType
    description: str = ""
    reference_id: Optional[str] = None

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError(f"Transaction amount must be positive, got {self.amount}")
        if self.reference_id is None:
            self.reference_id = str(uuid.uuid4())


@dataclass
class TransactionResult:
    success: bool
    transaction_id: str
    new_balance: float
    message: str = ""


class TransactionProcessor:
    def __init__(self, balance: float, currency: str = "USD", daily_limit: float = 5000.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = balance
        self.currency = currency
        self.daily_limit = daily_limit
        self._daily_spent = 0.0
        self._transaction_history: list[Transaction] = []

    def process(self, transaction: Transaction) -> TransactionResult:
        transaction_id = str(uuid.uuid4())

        if transaction.transaction_type == TransactionType.DEBIT:
            return self._process_debit(transaction, transaction_id)
        elif transaction.transaction_type == TransactionType.CREDIT:
            return self._process_credit(transaction, transaction_id)
        else:
            raise ValueError(f"Unsupported transaction type: {transaction.transaction_type}")

    def _process_debit(self, transaction: Transaction, transaction_id: str) -> TransactionResult:
        if transaction.amount > self.balance:
            return TransactionResult(
                success=False,
                transaction_id=transaction_id,
                new_balance=self.balance,
                message="Insufficient funds",
            )

        if self._daily_spent + transaction.amount > self.daily_limit:
            return TransactionResult(
                success=False,
                transaction_id=transaction_id,
                new_balance=self.balance,
                message="Daily limit exceeded",
            )

        self.balance = round(self.balance - transaction.amount, 2)
        self._daily_spent += transaction.amount
        self._transaction_history.append(transaction)

        return TransactionResult(
            success=True,
            transaction_id=transaction_id,
            new_balance=self.balance,
        )

    def _process_credit(self, transaction: Transaction, transaction_id: str) -> TransactionResult:
        self.balance = round(self.balance + transaction.amount, 2)
        self._transaction_history.append(transaction)

        return TransactionResult(
            success=True,
            transaction_id=transaction_id,
            new_balance=self.balance,
        )

    def get_transaction_count(self) -> int:
        return len(self._transaction_history)

    def reset_daily_limit(self) -> None:
        self._daily_spent = 0.0
