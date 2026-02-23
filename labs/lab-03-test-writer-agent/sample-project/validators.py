import re
from typing import Optional


def validate_amount(amount) -> float:
    if amount is None:
        raise ValueError("Amount cannot be None")
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        raise TypeError(f"Amount must be a number, got {type(amount).__name__}")
    if amount <= 0:
        raise ValueError(f"Amount must be positive, got {amount}")
    if amount > 1_000_000:
        raise ValueError(f"Amount exceeds maximum allowed value of 1,000,000")
    return round(amount, 2)


def validate_account_number(account_number: str) -> str:
    if not account_number:
        raise ValueError("Account number cannot be empty")
    cleaned = account_number.replace("-", "").replace(" ", "")
    if not cleaned.isdigit():
        raise ValueError("Account number must contain only digits and hyphens")
    if len(cleaned) < 8 or len(cleaned) > 16:
        raise ValueError("Account number must be between 8 and 16 digits")
    return cleaned


def validate_currency_code(code: str) -> str:
    if not code:
        raise ValueError("Currency code cannot be empty")
    code = code.upper().strip()
    if not re.match(r'^[A-Z]{3}$', code):
        raise ValueError("Currency code must be exactly 3 uppercase letters (e.g., USD, EUR)")
    return code


def validate_description(description: Optional[str], max_length: int = 200) -> str:
    if description is None:
        return ""
    description = description.strip()
    if len(description) > max_length:
        raise ValueError(f"Description cannot exceed {max_length} characters")
    return description
