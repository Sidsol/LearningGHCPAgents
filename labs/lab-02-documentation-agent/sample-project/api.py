from datetime import date
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from expense_tracker import ExpenseTracker
from models import Category

app = FastAPI(title="Expense Tracker API")
tracker = ExpenseTracker()


class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: str
    date: Optional[date] = None


class ExpenseResponse(BaseModel):
    amount: float
    category: str
    description: str
    date: date


@app.post("/expenses", response_model=ExpenseResponse, status_code=201)
def create_expense(expense_data: ExpenseCreate):
    try:
        category = Category(expense_data.category)
    except ValueError:
        valid = [c.value for c in Category]
        raise HTTPException(status_code=422, detail=f"Invalid category. Must be one of: {valid}")

    expense = tracker.add_expense(
        amount=expense_data.amount,
        category=category,
        description=expense_data.description,
        expense_date=expense_data.date,
    )
    return ExpenseResponse(
        amount=expense.amount,
        category=expense.category.value,
        description=expense.description,
        date=expense.date,
    )


@app.get("/expenses", response_model=list[ExpenseResponse])
def list_expenses(category: Optional[str] = None):
    if category:
        try:
            cat = Category(category)
        except ValueError:
            valid = [c.value for c in Category]
            raise HTTPException(status_code=422, detail=f"Invalid category. Must be one of: {valid}")
        expenses = tracker.get_by_category(cat)
    else:
        expenses = tracker.expenses

    return [
        ExpenseResponse(
            amount=e.amount,
            category=e.category.value,
            description=e.description,
            date=e.date,
        )
        for e in expenses
    ]


@app.get("/expenses/total")
def get_total():
    return {"total": tracker.get_total(), "currency": tracker.currency}


@app.get("/expenses/summary/{year}/{month}")
def get_monthly_summary(year: int, month: int):
    if not 1 <= month <= 12:
        raise HTTPException(status_code=422, detail="Month must be between 1 and 12")
    return tracker.get_monthly_summary(year, month)


@app.delete("/expenses")
def clear_expenses():
    tracker.clear()
    return {"message": "All expenses cleared"}
