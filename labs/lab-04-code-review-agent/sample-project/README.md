# Lab 4 Sample Project – Intentionally Flawed Code

> ⚠️ **IMPORTANT: This code is intentionally insecure and broken!**
>
> The Python files in this directory contain **deliberate security vulnerabilities and code quality issues** that exist for educational purposes. They are the subject of the code review exercise in Lab 4.

## Files and Their Intentional Issues

### `config.py`
- Hardcoded database passwords, API keys, JWT secrets (all use obvious `EXAMPLE_*` placeholders)
- Production credentials exposed in source code instead of environment variables
- Debug mode enabled in production configuration

### `user_service.py`
- SQL injection vulnerabilities (string concatenation in queries)
- Insecure password hashing (MD5)
- Sensitive data logged in plaintext (passwords)
- Bare `except:` clauses swallowing all errors
- Missing authentication on admin operations
- Mutable default argument (`results=[]`)

### `data_processor.py`
- N+1 query pattern (lookup inside a loop)
- Unnecessary O(n²) operations where O(n) is possible
- Repeated expensive computations inside loops
- Magic numbers without named constants
- Missing error handling for file I/O
- Unclear variable names (`x`, `r`)

---

## How to Use This Code

Use it as input for the **code-review-agent** and **security-agent** from Lab 4:

1. Run the code review agent on these files
2. Compare the agent's findings to the known issues listed above
3. Evaluate: did the agent catch everything? Did it flag anything incorrectly?

---

## ⛔ Do Not Use in Production

None of this code should ever be deployed or used in any real application. It exists solely to demonstrate what a good code review agent should catch.
