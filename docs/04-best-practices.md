# Best Practices for Writing Agent Profiles

These lessons come from analyzing 2,500+ real-world agent profiles across open-source and enterprise repositories. Apply these practices to write agents that are reliable, predictable, and genuinely useful.

---

## 1. Define a Hyper-Specific Persona

The #1 mistake teams make: writing a vague persona.

❌ **Avoid:**
```markdown
You are a helpful coding assistant.
```

✅ **Do this instead:**
```markdown
You are a TypeScript engineer specializing in Next.js 14 applications using the App Router.
You write React Server Components by default and only use client components when interactivity
is explicitly required. You follow our team's component naming conventions (PascalCase for
components, camelCase for utilities) and never use any-typed variables.
```

The more specific the persona, the more predictable the output. A generic assistant gives generic answers. A specialist gives specialist answers.

---

## 2. Be Explicit About Boundaries (What NOT to Do)

This is the most underrated practice. Great agents have clear **negative constraints** — explicit rules about what they should NOT do.

❌ **Missing boundaries:**
```markdown
You write unit tests for Python code.
```

✅ **With clear boundaries:**
```markdown
You write pytest unit tests for Python code.

DO NOT:
- Modify any file outside of the `tests/` directory
- Modify `conftest.py` unless explicitly asked
- Write integration tests or end-to-end tests
- Remove existing tests — only add new ones
- Use external network calls in tests (mock all external dependencies)
```

Boundaries prevent agents from making unexpected changes that require manual cleanup.

---

## 3. Supply Examples in the Prompt

Examples are the fastest way to calibrate agent behavior. Show the agent exactly what success looks like.

```markdown
## Example Output

When writing a test for this function:
```python
def calculate_discount(price: float, discount_pct: float) -> float:
    if discount_pct < 0 or discount_pct > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_pct / 100)
```

Write tests like this:
```python
class TestCalculateDiscount:
    """Tests for the calculate_discount function."""

    def test_standard_discount(self):
        """Apply a standard percentage discount."""
        assert calculate_discount(100.0, 20.0) == 80.0

    def test_zero_discount(self):
        """Zero discount returns original price."""
        assert calculate_discount(100.0, 0.0) == 100.0

    def test_invalid_discount_raises(self):
        """Negative discount raises ValueError."""
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            calculate_discount(100.0, -5.0)
```
```

---

## 4. Specify Tool Access Explicitly

Restricting tools limits the blast radius of mistakes.

```yaml
# Good: explicit, minimal permissions
tools: ["read", "edit", "search"]

# Risky: agent can run shell commands, create PRs, etc.
# (omitting tools = all tools available)
```

**Rule of thumb:** Grant the minimum tools needed for the task. A documentation agent doesn't need `run_in_terminal`. A test writer doesn't need `create_pull_request` unless you want automated PRs.

---

## 5. Structure Your Prompt for Scannability

Use headings, lists, and code blocks. Agents process these well, and it makes the profile easier for humans to maintain.

```markdown
## Role
[Who the agent is]

## Scope
[What it works on and doesn't work on]

## Instructions
[How to do the work]

## Output Format
[What the output should look like]

## Examples
[Concrete examples of expected behavior]

## What to Avoid
[Explicit anti-patterns and prohibited actions]
```

---

## 6. Match Agent Scope to Task Complexity

| Task Complexity | Agent Scope | Example |
|----------------|-------------|---------|
| Simple, atomic | Single responsibility | "Only write docstrings" |
| Medium | Domain specialist | "Handle all testing for auth module" |
| Complex | Multi-domain with handoffs | "Plan + implement + test a feature" |

Resist the urge to create a "do everything" agent. Multiple focused agents outperform one sprawling agent.

---

## 7. Version Your Agent Profiles

Treat agent profiles like code — they should go through code review and have a clear change history.

```markdown
---
name: test-writer-agent
description: Writes pytest tests for Python functions (v2 - added edge case requirements)
---
<!-- Changelog:
  v2 (2025-06): Added edge case requirements, added mocking instructions
  v1 (2025-03): Initial release
-->
```

---

## 8. Test Your Agent Profiles

Before rolling out to the team, test the agent on real tasks:

1. **Happy path:** Does it handle the standard case well?
2. **Edge cases:** What happens with unusual inputs?
3. **Boundary conditions:** Does it respect its "do not" rules?
4. **Failure modes:** What does it do when it's confused or blocked?

Document the results and iterate on the prompt.

---

## 9. Organizational Patterns

### Pattern A: One Agent Per Role

```
.github/agents/
├── documentation-agent.agent.md   ← Docs team uses this
├── test-writer-agent.agent.md     ← Backend team uses this
├── frontend-agent.agent.md        ← Frontend team uses this
└── security-agent.agent.md        ← Security team uses this
```

Best for: Teams with clear role divisions.

### Pattern B: One Agent Per Workflow Stage

```
.github/agents/
├── plan-agent.agent.md     ← Breaks down requirements into tasks
├── implement-agent.agent.md ← Writes the implementation
├── test-agent.agent.md     ← Writes the tests
└── review-agent.agent.md   ← Reviews before PR
```

Best for: Teams that want AI involvement at every stage of the SDLC.

### Pattern C: Stack-Specific Agents

```
.github/agents/
├── python-backend-agent.agent.md
├── react-frontend-agent.agent.md
└── terraform-infrastructure-agent.agent.md
```

Best for: Full-stack teams where each layer has very different conventions.

---

## 10. Common Anti-Patterns to Avoid

### Anti-Pattern: The "Do Everything" Agent

```markdown
# ❌ Too broad — unpredictable behavior
---
name: coding-agent
description: Helps with all coding tasks
---
You are a helpful coding assistant that can write code, review code, 
write tests, update documentation, fix bugs, and optimize performance.
```

**Problem:** No clear boundaries = inconsistent, often unhelpful results.

### Anti-Pattern: The Authoritarian Agent

```markdown
# ❌ Too many rules make the agent confused
DO NOT modify files in src/
DO NOT modify files in tests/
DO NOT modify configuration files
DO NOT create new files
DO NOT delete files
DO NOT run any commands
```

**Problem:** If an agent can't do anything, it can't help.

### Anti-Pattern: The Assumption-Heavy Agent

```markdown
# ❌ Assumes context the agent doesn't have
You know our internal systems. Use the standard approach we've discussed.
```

**Problem:** Agents don't have memory between sessions. Provide all context explicitly.

### Anti-Pattern: The Underspecified Agent

```markdown
# ❌ Not enough detail
---
description: Writes good code
---
Write good, clean code following best practices.
```

**Problem:** "Good code" and "best practices" are subjective. Be specific.

---

## 11. The Iterative Improvement Loop

Agent profiles are living documents. Follow this cycle:

```
1. Write a first draft
      ↓
2. Test on 5-10 real tasks
      ↓
3. Note where it fails or produces poor output
      ↓
4. Add specific instructions to address failures
      ↓
5. Add examples for recurring patterns
      ↓
6. Re-test and repeat
      ↓
7. Share improved profile with team
```

Most good agent profiles go through 3–5 iterations before they're production-ready.

---

## 12. Community Resources for Inspiration

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)** — Collection of community-contributed agent profiles for common languages and frameworks. Browse before building from scratch.

- **GitHub Copilot documentation** — The [configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration) has detailed specs for all YAML properties.

- **Your team's own profiles** — After building a few agents, your own patterns become your best reference.

---

## Quick Reference Checklist

Before publishing a custom agent, verify:

- [ ] Description clearly explains what the agent does and doesn't do
- [ ] Persona is specific (not "helpful assistant")
- [ ] Boundaries explicitly list what the agent should NOT do
- [ ] Tools are explicitly specified (not default "all tools")
- [ ] At least one concrete example is included in the prompt
- [ ] Prompt uses headings and lists for structure
- [ ] Agent has been tested on at least 5 real tasks
- [ ] Profile has been reviewed by at least one other team member

---

➡️ **Ready to build?** Start with [Lab 1 – Your First Custom Agent](../labs/lab-01-hello-agent/README.md)
