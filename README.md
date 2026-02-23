# 🤖 Learning GitHub Copilot Custom Agents

> An interactive, hands-on guide for engineering teams to understand, build, and leverage GitHub Copilot custom agents to supercharge their workflows.

---

## 🎯 What This Repository Is About

This repository is a **practical learning resource** designed to help your team understand GitHub Copilot custom agents — what they are, why they matter, and how to use them effectively. It includes conceptual documentation, real-world examples, and guided hands-on labs.

**By the end, your team will be able to:**
- Explain what custom agents are and why they're powerful
- Identify when to use a custom agent vs. plain Copilot
- Build and deploy a custom agent profile for your own workflows
- Reuse community-contributed agents from open-source libraries

---

## 📚 Table of Contents

| Section | Description |
|---------|-------------|
| [Why Custom Agents?](docs/01-why-custom-agents.md) | The case for custom agents and their business value |
| [When to Use Them](docs/02-when-to-use.md) | Decision guide: when agents shine vs. when they don't |
| [How They Work](docs/03-how-agents-work.md) | Agent profiles, YAML frontmatter, tools, and MCP servers |
| [Best Practices](docs/04-best-practices.md) | Lessons learned from 2,500+ real-world repositories |
| **Labs** | |
| [Lab 1 – Hello Agent](labs/lab-01-hello-agent/README.md) | Your first custom agent profile in 5 minutes |
| [Lab 2 – Documentation Agent](labs/lab-02-documentation-agent/README.md) | Build an agent that writes & maintains docs |
| [Lab 3 – Test Writer Agent](labs/lab-03-test-writer-agent/README.md) | Build an agent that generates tests |
| [Lab 4 – Code Review Agent](labs/lab-04-code-review-agent/README.md) | Build an agent that reviews PRs for style and quality |
| **Examples** | |
| [Agent Profile Examples](examples/) | Ready-to-use agent profiles for common tasks |
| [`.github/agents/`](.github/agents/) | Live agent profiles active in this repository |

---

## 🚀 Quick Start

### Prerequisites
- A GitHub account with Copilot access (Pro, Business, or Enterprise)
- Basic familiarity with Markdown and YAML

### Start Here

1. **Read the overview** → [Why Custom Agents?](docs/01-why-custom-agents.md)
2. **Work through Lab 1** → [Hello Agent](labs/lab-01-hello-agent/README.md)
3. **Pick a use case** → [Examples Library](examples/)
4. **Apply it to your work** → copy an example into your own repo's `.github/agents/` folder

---

## 🗂️ Repository Structure

```
LearningGHCPAgents/
├── README.md                         ← You are here
├── .github/
│   └── agents/                       ← Live custom agent profiles
│       ├── documentation-agent.agent.md
│       ├── test-writer-agent.agent.md
│       ├── code-review-agent.agent.md
│       └── security-agent.agent.md
├── docs/                             ← Conceptual documentation
│   ├── 01-why-custom-agents.md
│   ├── 02-when-to-use.md
│   ├── 03-how-agents-work.md
│   └── 04-best-practices.md
├── labs/                             ← Hands-on exercises
│   ├── lab-01-hello-agent/
│   ├── lab-02-documentation-agent/
│   ├── lab-03-test-writer-agent/
│   └── lab-04-code-review-agent/
└── examples/                         ← Ready-to-use agent profiles
    ├── minimal-agent.agent.md
    ├── full-stack-agent.agent.md
    ├── security-agent.agent.md
    └── devops-agent.agent.md
```

---

## 🧠 Key Concepts at a Glance

### What Is a Custom Agent?

A **custom agent** is a specialized version of the Copilot coding agent that you define once using a Markdown file called an **agent profile**. Instead of repeating instructions every session, you encode your team's conventions, tools, and standards directly into Copilot's behavior.

Think of it as giving Copilot a **job description and employee handbook** for a specific role on your team.

### Why Does This Matter?

| Without Custom Agents | With Custom Agents |
|----------------------|-------------------|
| Repeat context every session | Agent knows your stack and conventions |
| Inconsistent code style across contributors | Agent enforces standards automatically |
| Slow onboarding for new developers | Agent embeds team knowledge |
| Manual repetitive tasks (docs, tests, reviews) | Agent handles them autonomously |

### When Should You Use One?

Use a custom agent when you find yourself:
- ✅ Repeating the same instructions to Copilot
- ✅ Wanting Copilot to always follow specific conventions
- ✅ Automating a well-defined, repeatable task
- ✅ Needing domain-specific expertise (security, testing, docs)

---

## 🛠️ The Agent Profile Format

Agent profiles are Markdown files with YAML frontmatter stored in `.github/agents/`:

```markdown
---
name: my-agent
description: A brief description of what this agent does
tools: ["read", "edit", "search"]
---

You are a [role description]. Your job is to [specific task].

Follow these guidelines:
- [Rule 1]
- [Rule 2]
- [Rule 3]
```

Agents can be triggered:
- From the **Copilot Agents tab** on GitHub.com
- From **VS Code**, **JetBrains**, **Eclipse**, or **Xcode**
- Via **GitHub Copilot CLI**
- By **assigning a Copilot agent to a GitHub Issue**

---

## 🌐 Community Resources

- 📖 [Official Docs – About Custom Agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)
- 📖 [Official Docs – Creating Custom Agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- ⭐ [github/awesome-copilot](https://github.com/github/awesome-copilot) – Community-contributed agent profiles
- 📝 [Custom Agents in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

---

## 🤝 How to Contribute to This Repo

1. Fork this repository
2. Add a new lab or example agent profile
3. Open a pull request — try using the **code-review-agent** on your own PR!

---

*Happy building! 🚀 Custom agents are your team's superpower for consistent, scalable, AI-powered development.*