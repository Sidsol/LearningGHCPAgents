# How Agents Work: The Technical Details

## Overview

Custom agents are defined using **agent profiles** — Markdown files with YAML frontmatter. When a developer invokes an agent, GitHub Copilot reads the profile and uses it to configure the AI's behavior, available tools, and instructions for that session.

---

## File Location & Naming

Agent profiles must be stored in the `.github/agents/` directory of your repository. They use the `.agent.md` extension.

```
your-repo/
└── .github/
    └── agents/
        ├── documentation-agent.agent.md
        ├── test-writer-agent.agent.md
        └── security-agent.agent.md
```

**Naming rules:**
- Only use characters: `.`, `-`, `_`, `a-z`, `A-Z`, `0-9`
- The filename (without `.agent.md`) becomes the agent's default name
- Names must be unique within the repository

**Scope levels:**
| Level | Location | Availability |
|-------|----------|--------------|
| Repository | `.github/agents/NAME.agent.md` | Only in that repository |
| Organization/Enterprise | `/agents/NAME.agent.md` in `.github-private` repo | All repos in org/enterprise |

---

## The Agent Profile Structure

An agent profile has two sections:

```markdown
---
# YAML Frontmatter (metadata and configuration)
name: my-agent
description: What this agent does
tools: ["read", "edit", "search"]
---

<!-- Markdown content below the frontmatter = the agent's prompt -->

You are a [role description]...
```

---

## YAML Frontmatter Properties

### `name` (optional)
A human-readable display name for the agent. Defaults to the filename without the `.agent.md` suffix.

```yaml
name: Python Test Engineer
```

### `description` (required)
A brief explanation of the agent's purpose. This appears in the Copilot UI when browsing available agents.

```yaml
description: Writes pytest unit tests for Python functions following PEP 8 and our team's testing patterns
```

### `tools` (optional)
A list of tools the agent is allowed to use. If omitted, the agent has access to **all** available tools (built-in tools + MCP server tools).

```yaml
tools:
  - read       # Read files
  - edit       # Write/modify files
  - search     # Search the codebase
  - run_tests  # Execute test commands
```

**Available built-in tools include:**
| Tool | Description |
|------|-------------|
| `read` | Read file contents |
| `edit` | Create and modify files |
| `search` | Search across the codebase |
| `run_in_terminal` | Execute shell commands |
| `create_pull_request` | Open PRs on GitHub |
| `fetch` | Fetch web content |
| `github` | Interact with GitHub APIs |

> 💡 **Best Practice:** Explicitly define only the tools your agent needs. Restricting tools reduces the risk of unintended side effects.

### `model` (VS Code / JetBrains only)
Specify which AI model the agent should use.

```yaml
model: gpt-4o
```

### `target` (optional)
Restrict the agent to a specific environment.

```yaml
target: github-copilot  # Only available on GitHub.com
# OR
target: vscode          # Only available in VS Code
```

### `mcp-servers` (organization/enterprise only)
Configure MCP (Model Context Protocol) servers that extend the agent's capabilities with custom tools.

```yaml
mcp-servers:
  - name: my-internal-tools
    url: https://my-tools.company.internal/mcp
```

---

## The Prompt Section

Below the YAML frontmatter, the Markdown content becomes the agent's **system prompt** — the core instructions that define its behavior.

### Anatomy of a Good Prompt

```markdown
---
name: python-test-engineer
description: Writes pytest tests for Python code following our team standards
tools: ["read", "edit", "search"]
---

## Role
You are a Python testing specialist focused exclusively on writing and improving
pytest unit tests. You do not modify production code.

## Scope
- ONLY create or modify files in the `tests/` directory
- NEVER modify files outside of `tests/` (no __init__.py, no models, no config)
- Focus on unit tests; do not write integration or end-to-end tests

## Testing Standards
- Use pytest fixtures for setup and teardown
- Follow the Arrange-Act-Assert (AAA) pattern
- Name test functions as `test_<function_name>_<scenario>`
- Aim for 80%+ coverage of the target function
- Include at least one edge case per function

## Output Format
When writing tests:
1. Start with a brief comment explaining what is being tested
2. Group related tests in a class if there are more than 3 tests for one function
3. Add docstrings to test classes explaining the test scenario

## What to Avoid
- Do not write tests that depend on external services without mocking
- Do not use `assert True` or trivially passing assertions
- Do not skip writing error path tests
```

### Prompt Length Limit
The prompt can be a **maximum of 30,000 characters**. This is generous — most agent prompts are 500–2,000 characters.

---

## How Agents Are Invoked

### On GitHub.com
1. Navigate to the [Copilot Agents tab](https://github.com/copilot/agents)
2. Click the agent selector dropdown
3. Choose your custom agent
4. Describe the task — the agent handles the rest

### In VS Code
1. Open GitHub Copilot Chat
2. Click the `@` mention or agent dropdown at the bottom of the chat
3. Select your custom agent
4. Type your request

### By Assigning to a GitHub Issue
1. Open any GitHub issue
2. Click **Assign Copilot** in the assignees panel
3. Select your custom agent from the dropdown
4. The agent reads the issue and begins working

### Via Copilot CLI
```bash
gh copilot suggest --agent my-agent "write tests for the new auth module"
```

---

## How the Agent Processes a Task

When you invoke a custom agent with a task, here's what happens under the hood:

```
1. You describe the task (e.g., "Write tests for user_service.py")
      ↓
2. Copilot combines:
   - Your task description
   - The agent's prompt (from the agent profile)
   - Current repository context
      ↓
3. The agent uses its tools to:
   - Read relevant files
   - Understand the codebase structure
   - Plan the changes needed
      ↓
4. The agent executes changes:
   - Creates/modifies files
   - Runs tests (if authorized)
   - Opens a PR (if configured)
      ↓
5. You review the results and provide feedback
```

---

## Agent Profiles vs. Custom Instructions

It's worth distinguishing between agent profiles and GitHub Copilot's custom instructions (`.github/copilot-instructions.md`):

| Feature | Agent Profile | Custom Instructions |
|---------|--------------|---------------------|
| File location | `.github/agents/*.agent.md` | `.github/copilot-instructions.md` |
| Scope | Specific task/role | All Copilot interactions |
| Tools control | Yes | No |
| Multiple per repo | Yes (one per file) | No (one file) |
| On/off toggle | Yes (select the agent) | Always active |
| Best for | Specialized tasks | General conventions |

> 💡 **Tip:** Use `.github/copilot-instructions.md` for universal team conventions (like "we use TypeScript"), and custom agents for specific task types (like "write tests" or "review PRs").

---

## Practical Configuration Examples

### Minimal Agent (just a prompt)
```markdown
---
description: Summarizes pull request changes in plain English for non-technical stakeholders
---

You summarize pull request diffs in 2–3 plain sentences that a non-engineer can understand.
Focus on the user-facing impact, not the technical implementation details.
```

### Constrained Agent (specific tools)
```markdown
---
name: security-scanner
description: Scans code for security vulnerabilities and OWASP Top 10 issues
tools: ["read", "search"]
---

You are a security specialist. You ONLY read and analyze code — never modify it.
...
```

### Full-Featured Agent (tools + MCP)
```markdown
---
name: devops-agent
description: Manages CI/CD pipelines, deployment configs, and infrastructure-as-code
tools: ["read", "edit", "run_in_terminal", "github"]
mcp-servers:
  - name: kubernetes-tools
    url: https://k8s-mcp.company.internal
---

You are a DevOps engineer specializing in our Kubernetes-based infrastructure...
```

---

## Summary

| Concept | Key Point |
|---------|-----------|
| File format | Markdown with YAML frontmatter |
| Location | `.github/agents/*.agent.md` |
| Required fields | `description` |
| Tools | Default: all tools; specify to restrict |
| Prompt | Plain Markdown, up to 30,000 characters |
| Invocation | GitHub UI, VS Code, JetBrains, CLI, or Issue assignment |

---

➡️ **Next:** [Best Practices for Writing Agent Profiles](04-best-practices.md)
