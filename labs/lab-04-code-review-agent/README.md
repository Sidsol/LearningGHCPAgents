# Lab 4: Code Review Agent

> **Difficulty:** Intermediate–Advanced  
> **Time:** 45–60 minutes  
> **Prerequisites:** Completed Labs 1–3

---

## 🎯 Objectives

By the end of this lab, you will:
1. Build a code review agent that enforces team standards automatically
2. Learn how to encode different review dimensions (style, security, performance)
3. Understand the difference between reporting issues vs. fixing them
4. Create a repeatable, consistent PR review process with AI

---

## 📖 The Scenario

Your team gets 15–20 pull requests per week. Code reviews take 45 minutes to 2 hours each. Half of that time is spent on comments about style, naming conventions, missing error handling, and security patterns — things that are mechanical and rules-based.

Your goal: Build a code review agent that handles the **mechanical parts** of code review, so your human reviewers can focus on **architecture, business logic, and design**.

---

## 📂 The Sample Project

The sample project has some intentionally flawed code in [`sample-project/`](sample-project/). It contains common issues that a code review agent should catch:

```
sample-project/
├── user_service.py     ← Has security, style, and error handling issues
├── data_processor.py  ← Has performance and style issues
└── config.py          ← Has security issues (hardcoded credentials!)
```

---

## 🔧 Step 1: Define Your Review Standards

Before building the agent, write down what your team cares about:

**Security:**
- No hardcoded credentials or API keys
- SQL queries must use parameterized statements
- User inputs must be validated and sanitized
- No `eval()` or `exec()` on user input

**Code Style:**
- Follow PEP 8 for Python
- Functions must have type hints
- All public functions must have docstrings
- No bare `except:` clauses

**Error Handling:**
- Catch specific exceptions, not `BaseException`
- Log errors with context, not just silently swallow them
- Return meaningful error messages to callers

**Performance:**
- Avoid N+1 query patterns
- Use generators for large data sets
- Avoid unnecessary recomputation in loops

---

## 🏗️ Step 2: Review the Pre-Built Agent

👉 **[code-review-agent.agent.md](code-review-agent.agent.md)**

Notice how the agent:
1. Reports issues rather than fixing them (it's a reviewer, not an implementer)
2. Categorizes issues by severity (critical, warning, suggestion)
3. Provides actionable feedback with fix examples
4. Doesn't rewrite the code wholesale

---

## 🚀 Step 3: Run the Agent on Sample Code

Try these prompts:

### Prompt 1: Full PR Review
```
"Review the code in sample-project/ and provide a structured code review report"
```

### Prompt 2: Security-Focused Review
```
"Review user_service.py for security issues and provide a detailed security audit"
```

### Prompt 3: Quick Style Check
```
"Check config.py for any issues and flag critical problems"
```

---

## 📊 Step 4: Evaluate the Review Output

A good code review agent output should:

| Criterion | Expected |
|-----------|----------|
| **Finds all critical issues** | All hardcoded credentials, SQL injection risks, missing validation |
| **Severity is calibrated** | Not everything is "critical" — minor style issues are "suggestions" |
| **Actionable feedback** | Each issue has a suggested fix or reference |
| **Organized output** | Grouped by file, then by severity |
| **No false positives** | Doesn't flag correct code as problematic |

---

## 🔄 Step 5: Compare to Manual Review

Do a manual review of the sample code yourself. Compare what you found to what the agent found:

- Did the agent catch everything you found?
- Did the agent flag anything you wouldn't have?
- Are the suggested fixes correct?
- How long did the agent take vs. your manual review?

---

## 🔧 Step 6: Customize for Your Team

The code review agent in this lab is generic Python. To make it useful for your team, add:

```markdown
## Our Team's Specific Rules
- We use `structlog` for logging, not the stdlib `logging` module
- All database queries must go through the `db.query()` helper, not raw SQLAlchemy
- API endpoints must use our `@require_auth` decorator
- All public functions must include a `#noqa` comment if they intentionally break a rule
```

---

## 📝 Key Takeaways

- ✅ Code review agents work best when they report issues with severity levels, not just fix everything
- ✅ Encoding your team's specific rules makes reviews far more relevant than generic style checkers
- ✅ A "report and suggest" pattern (not "rewrite everything") keeps humans in control
- ✅ Separating concerns (security vs. style vs. performance) makes the agent's output more organized
- ✅ The agent handles mechanical reviews so humans can focus on design and business logic

---

## 🏆 Bonus Challenges

### Bonus 1: Auto-Fix Mode
Create a second agent (`code-fixer-agent`) that takes the code review report and applies the suggested fixes. Keep the review agent and fixer agent separate.

### Bonus 2: PR Summary Generator
Extend the code review agent to also generate a plain-English summary of the changes for stakeholders.

### Bonus 3: Architecture Review
Add instructions for the agent to flag violations of specific architectural patterns (e.g., "services must not import from other services directly").

---

## 📚 Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — Security review checklist
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Best Practices for Agent Prompts](../../docs/04-best-practices.md)

---

## 🎉 Congratulations!

You've completed all four labs! You now know how to:
- Create custom agent profiles for specialized tasks
- Encode team standards into agent instructions
- Build agents for documentation, testing, and code review
- Iterate on agent prompts to improve quality

### Next Steps

1. **Apply these agents to your real projects** — copy the agent profiles you built to your team's repositories
2. **Browse community agents** — check [github/awesome-copilot](https://github.com/github/awesome-copilot) for more inspiration
3. **Build your own** — what repetitive task in your workflow could benefit from a custom agent?

---

↩️ **Back to:** [Repository Overview](../../README.md)
