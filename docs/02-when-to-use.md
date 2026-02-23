# When to Use Custom Agents: A Decision Guide

## The Core Question

> **"Should I build a custom agent for this, or just use Copilot directly?"**

This document gives you a practical framework to answer that question.

---

## The Decision Framework

### ✅ Build a Custom Agent When...

#### 1. You repeat the same instructions more than 3 times
If you've typed "always use our logging library", "don't modify the config files", or "follow our React component pattern" more than a few times, it's time for an agent. Repetition is the clearest signal.

**Signal:** You have a mental checklist you recite to Copilot at the start of tasks.

#### 2. You're enforcing team standards
When multiple developers need to follow the same conventions, a custom agent ensures consistency across all of them — without relying on everyone remembering the rules.

**Signal:** You have a style guide, coding standards doc, or architecture decision records (ADRs).

#### 3. The task is well-defined and repeatable
Custom agents shine on tasks with clear inputs and outputs. "Write tests for this function" or "document this API endpoint" are perfect. "Think creatively about our product direction" is not.

**Signal:** You could write a checklist of what success looks like for the task.

#### 4. Domain expertise is needed
Some tasks require deep knowledge of a specific domain: security vulnerabilities, accessibility standards, regulatory compliance, etc. An agent can be an expert so you don't have to be.

**Signal:** Your team has to slow down or bring in a specialist for certain kinds of tasks.

#### 5. You're onboarding new team members
A custom agent can serve as a 24/7 guide for new developers, answering questions about the codebase, conventions, and workflows in the team's language.

**Signal:** Onboarding takes more than a week and involves lots of "how does our team do X?" questions.

#### 6. You want to automate a workflow end-to-end
From reading an issue to writing code to opening a PR — agents can handle entire workflows with the right tools and instructions.

**Signal:** You have a multi-step workflow that follows a predictable pattern.

---

### ❌ Don't Build a Custom Agent When...

#### 1. The task is truly one-off
If you'll only do something once, the overhead of writing and maintaining an agent profile isn't worth it. Use Copilot Chat directly with inline context.

#### 2. The task requires human judgment or creativity
Agents are not good at "decide which architecture is better" or "choose the right product direction". Save agents for execution, not strategic decision-making.

#### 3. Requirements change frequently
If the rules are constantly changing, an agent profile becomes a maintenance burden. Wait for things to stabilize before encoding them.

#### 4. The agent would need broad, unconstrained access
If you can't define clear boundaries (what tools it should use, what files it should or shouldn't touch), the agent is more likely to cause harm than help.

---

## Common Use Case Categories

### Category 1: Documentation & Writing

| Use Case | Good Fit? | Why |
|----------|-----------|-----|
| Generate README files | ✅ Excellent | Well-defined output, clear conventions |
| Write API documentation | ✅ Excellent | Structured, repeatable |
| Update changelogs | ✅ Good | Consistent format |
| Write product strategy docs | ❌ Poor | Requires business judgment |

**Example agent:** `documentation-agent` — [See Lab 2](../labs/lab-02-documentation-agent/README.md)

### Category 2: Testing

| Use Case | Good Fit? | Why |
|----------|-----------|-----|
| Write unit tests | ✅ Excellent | Clear patterns, repeatable |
| Generate edge case tests | ✅ Good | Can follow defined categories |
| Write integration tests | ✅ Good | With clear boundaries defined |
| Decide what to test | ❌ Poor | Requires architectural judgment |

**Example agent:** `test-writer-agent` — [See Lab 3](../labs/lab-03-test-writer-agent/README.md)

### Category 3: Code Review

| Use Case | Good Fit? | Why |
|----------|-----------|-----|
| Style/convention compliance | ✅ Excellent | Rules-based |
| Security vulnerability detection | ✅ Excellent | Known patterns |
| Architecture review | ⚠️ Mixed | Rules-based aspects only |
| Performance optimization | ⚠️ Mixed | Needs profiling context |
| Business logic correctness | ❌ Poor | Requires domain knowledge |

**Example agent:** `code-review-agent` — [See Lab 4](../labs/lab-04-code-review-agent/README.md)

### Category 4: DevOps & Operations

| Use Case | Good Fit? | Why |
|----------|-----------|-----|
| Update dependency versions | ✅ Excellent | Follows patterns |
| Generate CI/CD configurations | ✅ Good | Template-based |
| Create deployment manifests | ✅ Good | Well-defined structure |
| Incident response decision-making | ❌ Poor | Requires context and judgment |

### Category 5: Security

| Use Case | Good Fit? | Why |
|----------|-----------|-----|
| Scan for known vulnerability patterns | ✅ Excellent | Rules-based |
| Check for secret/credential exposure | ✅ Excellent | Pattern matching |
| Compliance checks (SOC2, HIPAA, etc.) | ✅ Good | Well-defined checklists |
| Threat modeling | ❌ Poor | Requires creative adversarial thinking |

---

## The "Specificity Test"

Before building an agent, answer these five questions. If you can answer all five, you're ready to build:

1. **Who is this agent?** (e.g., "A Python testing specialist")
2. **What should it do?** (e.g., "Write pytest tests following our specific patterns")
3. **What should it NOT do?** (e.g., "Never modify production config files or __init__.py")
4. **What does success look like?** (e.g., "Tests pass, cover edge cases, follow naming conventions")
5. **What tools does it need?** (e.g., read files, edit files, run tests)

If you can't answer question 3 (what NOT to do), your agent scope is too broad.

---

## Scope Calibration: Narrow vs. Broad

### Too Narrow (Diminishing Returns)
```yaml
# This is too specific — the agent has almost nothing to do
description: Agent that only writes docstrings for Python functions named "process_data"
```

### Too Broad (Risk of Harm)
```yaml
# This is too vague — the agent may do unexpected things
description: An agent that helps with coding
```

### Just Right (Sweet Spot)
```yaml
# Clear domain, clear scope, clear boundaries
description: Agent specializing in writing pytest unit tests for our Django REST API.
             Only modifies files in the tests/ directory. Never modifies models.py or settings.py.
```

---

## Real-World Decision Examples

### Scenario A: "We keep writing the same boilerplate tests"
→ **Build it.** Repetitive, well-defined, consistent patterns = perfect agent use case.

### Scenario B: "We want help with a one-time database migration"
→ **Don't build it** (unless this migration type recurs). Use Copilot inline with context.

### Scenario C: "Our new engineers don't know how to set up the dev environment"
→ **Build it.** Onboarding guide + standard setup = excellent agent use case.

### Scenario D: "We want AI to decide our feature roadmap"
→ **Don't build it.** Strategic decisions require human judgment and business context.

### Scenario E: "We need consistent API documentation across 12 microservices"
→ **Build it.** Cross-team standardization at scale = strong agent use case.

---

## Summary

| Indicator | Action |
|-----------|--------|
| Repeating same context | Build an agent |
| Enforcing team standards | Build an agent |
| Well-defined, repeatable task | Build an agent |
| Domain expertise required | Build an agent |
| One-off task | Use Copilot directly |
| Requires creative/strategic judgment | Use Copilot directly |
| Rapidly changing requirements | Wait |
| Undefined boundaries | Define them first |

---

➡️ **Next:** [How Agents Work – The Technical Details](03-how-agents-work.md)
