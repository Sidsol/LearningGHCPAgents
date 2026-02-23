# Lab 3: Test Writer Agent

> **Difficulty:** Intermediate  
> **Time:** 45–60 minutes  
> **Prerequisites:** Completed Lab 2

---

## 🎯 Objectives

By the end of this lab, you will:
1. Build a custom agent that writes high-quality unit tests
2. Learn how to encode testing standards into an agent profile
3. Practice writing agent constraints that prevent unintended behavior
4. Understand how to guide an agent to test edge cases systematically

---

## 📖 The Scenario

Your team has a Python module for processing financial transactions. The code works, but **it has zero test coverage**. Your tech lead is pushing for 80%+ coverage before the next release.

Instead of writing all the tests manually, you'll build a **test writer agent** that knows:
- Your team's testing patterns (pytest + fixtures)
- Which edge cases to always consider (empty inputs, negative numbers, boundary values)
- Where tests should live and what they should be named
- What NOT to test (mocking external services, not real calls)

---

## 📂 The Sample Project

The sample project is in [`sample-project/`](sample-project/):

```
sample-project/
├── transaction_processor.py  ← Financial transaction logic (no tests!)
├── validators.py             ← Input validation functions (no tests!)
└── formatters.py             ← Output formatting utilities (no tests!)
```

---

## 🔧 Step 1: Understand What Makes a Good Test

Before building the agent, internalize these principles the agent will enforce:

### The AAA Pattern (Arrange-Act-Assert)
```python
def test_process_valid_transaction():
    # Arrange
    processor = TransactionProcessor(balance=1000.0)
    transaction = Transaction(amount=100.0, type="debit")

    # Act
    result = processor.process(transaction)

    # Assert
    assert result.success is True
    assert processor.balance == 900.0
```

### Edge Cases Your Agent Must Always Consider
1. **Empty/None inputs** — what happens with no data?
2. **Boundary values** — exactly at the limit (e.g., exactly 0, exactly max)
3. **Negative numbers** — if the domain doesn't allow them, test that they're rejected
4. **Type mismatches** — wrong types as inputs
5. **Overflow/underflow** — very large or very small numbers
6. **Concurrent operations** — (when relevant) what if two operations happen simultaneously?

---

## 🏗️ Step 2: Design the Test Writer Agent

The test writer agent for this lab must:

**Do:**
- Write pytest unit tests in `tests/` directory
- Use the Arrange-Act-Assert pattern
- Test happy path + at least 2 edge cases per function
- Use pytest fixtures for shared setup
- Mock all external service calls

**Not do:**
- Modify source code files
- Write integration tests
- Remove or modify existing tests
- Import from non-standard libraries the project doesn't already use

---

## ✏️ Step 3: Review the Pre-Built Agent

👉 **[test-writer-agent.agent.md](test-writer-agent.agent.md)**

Pay special attention to:
1. How the prompt encodes the AAA pattern with a concrete example
2. How edge case categories are enumerated explicitly
3. How mocking instructions prevent tests from making real external calls
4. The test naming convention requirements

---

## 🚀 Step 4: Deploy and Test

1. Copy `test-writer-agent.agent.md` to `.github/agents/` in your repository
2. Try these prompts:

### Prompt 1: Basic Test Generation
```
"Write pytest tests for the TransactionProcessor class in transaction_processor.py"
```

### Prompt 2: Targeted Edge Case Testing
```
"Write tests specifically for edge cases in the validate_amount function in validators.py"
```

### Prompt 3: Coverage-Driven Testing
```
"Write tests for formatters.py with at least 80% coverage"
```

---

## 📊 Step 5: Evaluate Test Quality

Run the generated tests (if you have Python + pytest installed):

```bash
cd sample-project
pip install pytest
pytest tests/ -v --tb=short
```

Evaluate:
- Do tests pass? (they should for the happy path)
- Are edge cases covered?
- Is the AAA pattern followed?
- Are there descriptive test names?

---

## 🔄 Step 6: Improve the Agent

The sample project has functions that deal with financial amounts. Try adding these instructions to the agent and observe how the output changes:

```markdown
## Financial Domain Rules
When testing financial functions:
- Always test with values that have more than 2 decimal places (e.g., 10.555)
- Always test with zero as a boundary value
- Always test rounding behavior explicitly
- Test currency conversion if applicable
```

---

## 📝 Key Takeaways

- ✅ Test agents work best with explicit patterns (AAA) shown as examples
- ✅ Enumerated edge case categories produce more comprehensive test coverage
- ✅ Clear scope constraints prevent the agent from modifying source code
- ✅ Mocking instructions are critical for keeping tests deterministic
- ✅ Naming convention requirements make test suites more navigable

---

## 🏆 Bonus Challenges

### Bonus 1: Parameterized Tests
Extend the agent to generate `@pytest.mark.parametrize` tests for functions with multiple valid inputs.

### Bonus 2: Coverage Report Integration
Add an instruction for the agent to identify which code paths aren't covered and write tests for them specifically.

### Bonus 3: Property-Based Testing
Extend the agent to use `hypothesis` for property-based testing where appropriate.

---

## 📚 Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Mocking in Python](https://docs.python.org/3/library/unittest.mock.html)
- [Best Practices for Agent Prompts](../../docs/04-best-practices.md)

---

➡️ **Next Lab:** [Lab 4 – Code Review Agent](../lab-04-code-review-agent/README.md)
