# Lab 2: Documentation Agent

> **Difficulty:** Beginner–Intermediate  
> **Time:** 30–45 minutes  
> **Prerequisites:** Completed Lab 1

---

## 🎯 Objectives

By the end of this lab, you will:
1. Build a documentation agent tailored to a real Python project
2. Understand how to read existing code to create accurate documentation
3. Learn how agent instructions interact with real code
4. Practice iterating on an agent prompt to improve output quality

---

## 📖 The Scenario

Your team has a Python module for a simple expense tracker API. The code is well-written, but **there's no documentation**. New team members can't figure out how to use it without asking around.

Your goal: Create a documentation agent that can automatically generate accurate, helpful documentation for this project.

---

## 📂 The Sample Project

The sample project is in [`sample-project/`](sample-project/). It contains:

```
sample-project/
├── expense_tracker.py    ← Main module (no docstrings!)
├── api.py                ← REST API layer (no docs)
└── models.py             ← Data models (no docs)
```

Look at the code in these files — notice:
- Functions have no docstrings
- There's no README
- The API endpoints are not documented

---

## 🔧 Step 1: Examine the Sample Project

Open and read through the sample files to understand the codebase:
- [expense_tracker.py](sample-project/expense_tracker.py)
- [api.py](sample-project/api.py)
- [models.py](sample-project/models.py)

**Questions to answer:**
1. What does the module do?
2. What are the main functions?
3. What would a new developer need to know to use this?

---

## 🏗️ Step 2: Design the Documentation Agent

Before writing the agent profile, think about:

**What should this agent do?**
- Generate README.md for the project
- Add docstrings to Python functions and classes
- Document API endpoints

**What should it NOT do?**
- Modify the actual logic of the code
- Change function signatures
- Delete existing content

**What context does it need?**
- The project uses Python 3.10+
- We follow Google-style docstrings
- We use FastAPI for the REST API layer

---

## ✏️ Step 3: Review the Pre-Built Agent

The lab includes a pre-built documentation agent:

👉 **[documentation-agent.agent.md](documentation-agent.agent.md)**

Read through it and notice how it encodes:
1. A specific persona
2. Clear scope boundaries
3. Docstring format requirements
4. Output quality standards

---

## 🚀 Step 4: Deploy the Agent

1. Copy `documentation-agent.agent.md` to `.github/agents/` in your own repository
2. Commit and merge to your default branch
3. Navigate to the repository in Copilot's agent interface

---

## 🧪 Step 5: Run the Agent

Try these prompts and observe the outputs:

### Task 1: Generate a README
```
"Create a comprehensive README for this expense tracker project"
```

### Task 2: Add Docstrings
```
"Add Google-style docstrings to all functions in expense_tracker.py"
```

### Task 3: Document the API
```
"Create an API reference document for the endpoints in api.py"
```

---

## 📊 Step 6: Evaluate the Output

For each task, evaluate the output against these criteria:

| Criterion | ✅ Pass | ❌ Fail |
|-----------|---------|---------|
| Accuracy | Correctly describes what the code does | Contains hallucinations or wrong info |
| Completeness | Covers all public functions/endpoints | Missing important elements |
| Format | Follows specified docstring style | Uses wrong format |
| Scope compliance | Only modified docs, not code logic | Changed actual code |
| Usefulness | A new developer would find this helpful | Too vague to be useful |

---

## 🔄 Step 7: Iterate on the Prompt

Based on your evaluation, try to improve the agent profile:

**If accuracy is poor:** Add an instruction to always read the code before writing documentation.

**If format is wrong:** Add a concrete example of a properly formatted docstring.

**If it's modifying code:** Add more explicit "NEVER modify X" constraints.

**If documentation is too generic:** Add instructions to include actual parameter types and return values from the code.

---

## 📝 Key Takeaways

- ✅ Documentation agents work best when they're told which format to follow (Google-style, NumPy-style, etc.)
- ✅ Providing a concrete example in the prompt dramatically improves format consistency
- ✅ "Read the code first" instructions make documentation more accurate
- ✅ Scope constraints prevent agents from accidentally modifying code while documenting it

---

## 🏆 Bonus Challenge

Extend the documentation agent to also:
1. Generate a `CHANGELOG.md` from commit messages
2. Keep the README in sync when new functions are added

Hint: You'll need to add `github` to the tools list to access commit history.

---

## 📚 Resources

- [Google Python Style Guide – Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Best Practices for Agent Prompts](../../docs/04-best-practices.md)

---

➡️ **Next Lab:** [Lab 3 – Test Writer Agent](../lab-03-test-writer-agent/README.md)
