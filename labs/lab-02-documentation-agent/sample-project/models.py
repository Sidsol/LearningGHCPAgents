from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class Category(Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    HOUSING = "housing"
    ENTERTAINMENT = "entertainment"
    HEALTH = "health"
    OTHER = "other"


@dataclass
class Expense:
    amount: float
    category: Category
    description: str
    date: date = field(default_factory=date.today)

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError(f"Amount must be positive, got {self.amount}")
