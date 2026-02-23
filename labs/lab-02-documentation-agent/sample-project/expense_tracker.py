from datetime import date, timedelta
from typing import Optional
from collections import defaultdict

from models import Expense, Category


class ExpenseTracker:
    def __init__(self, currency: str = "USD"):
        self.expenses: list[Expense] = []
        self.currency = currency

    def add_expense(self, amount: float, category: Category, description: str, expense_date: Optional[date] = None) -> Expense:
        expense = Expense(
            amount=amount,
            category=category,
            description=description,
            date=expense_date or date.today(),
        )
        self.expenses.append(expense)
        return expense

    def get_total(self) -> float:
        return round(sum(e.amount for e in self.expenses), 2)

    def get_by_category(self, category: Category) -> list[Expense]:
        return [e for e in self.expenses if e.category == category]

    def get_category_totals(self) -> dict[Category, float]:
        totals: dict[Category, float] = defaultdict(float)
        for expense in self.expenses:
            totals[expense.category] += expense.amount
        return {cat: round(total, 2) for cat, total in totals.items()}

    def get_expenses_in_range(self, start: date, end: date) -> list[Expense]:
        return [e for e in self.expenses if start <= e.date <= end]

    def get_monthly_summary(self, year: int, month: int) -> dict:
        start = date(year, month, 1)
        if month == 12:
            end = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            end = date(year, month + 1, 1) - timedelta(days=1)

        monthly_expenses = self.get_expenses_in_range(start, end)
        return {
            "period": f"{year}-{month:02d}",
            "total": round(sum(e.amount for e in monthly_expenses), 2),
            "count": len(monthly_expenses),
            "by_category": {
                cat.value: round(sum(e.amount for e in monthly_expenses if e.category == cat), 2)
                for cat in Category
                if any(e.category == cat for e in monthly_expenses)
            },
        }

    def remove_expense(self, expense: Expense) -> bool:
        try:
            self.expenses.remove(expense)
            return True
        except ValueError:
            return False

    def clear(self) -> None:
        self.expenses.clear()
