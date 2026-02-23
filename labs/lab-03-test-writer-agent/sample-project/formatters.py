from datetime import datetime
from typing import Optional


def format_currency(amount: float, currency: str = "USD", symbol: bool = True) -> str:
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥"}
    formatted = f"{amount:,.2f}"
    if symbol and currency in symbols:
        return f"{symbols[currency]}{formatted}"
    return f"{formatted} {currency}"


def format_transaction_id(transaction_id: str) -> str:
    if not transaction_id:
        raise ValueError("Transaction ID cannot be empty")
    clean = transaction_id.replace("-", "").upper()
    if len(clean) < 8:
        raise ValueError("Transaction ID is too short")
    return f"TXN-{clean[:8]}"


def format_date(dt: Optional[datetime] = None, fmt: str = "%Y-%m-%d") -> str:
    if dt is None:
        dt = datetime.utcnow()
    return dt.strftime(fmt)


def format_summary(total: float, count: int, currency: str = "USD") -> str:
    if count == 0:
        return "No transactions recorded."
    avg = total / count
    return (
        f"{count} transaction{'s' if count != 1 else ''} | "
        f"Total: {format_currency(total, currency)} | "
        f"Average: {format_currency(avg, currency)}"
    )
