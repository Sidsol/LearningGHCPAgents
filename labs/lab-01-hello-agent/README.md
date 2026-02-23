# Lab 1: Hello Agent – Your First Custom Agent Profile

> **Difficulty:** Beginner  
> **Time:** 15–20 minutes  
> **Prerequisites:** GitHub account with Copilot access  

---

## 🎯 Objectives

By the end of this lab, you will:
1. Understand the structure of an agent profile
2. Create your first `.agent.md` file from scratch
3. Invoke your agent in the GitHub Copilot interface
4. Observe how the agent's instructions shape Copilot's behavior

---

## 📖 Background

A custom agent is defined by a Markdown file called an **agent profile**. It lives in `.github/agents/` and uses YAML frontmatter to configure behavior.

The simplest possible agent profile looks like this:

```markdown
---
description: A friendly helper
---

You are a helpful assistant.
```

But useful agents are much more specific. In this lab, you'll build a "README Creator" agent that generates high-quality README files.

---

## 🏗️ Step 1: Understand the Template

Look at the agent profile included with this lab:

👉 **[my-first-agent.agent.md](my-first-agent.agent.md)**

Open it and read through each section. Notice:
- The YAML frontmatter (`---` block) contains configuration
- The Markdown below the frontmatter is the agent's instructions (prompt)
- The instructions are specific about what to do AND what not to do

---

## 🔧 Step 2: Explore the Anatomy

Here's the annotated structure:

```markdown
---
name: readme-creator          ← Display name in the Copilot UI
description: Creates README   ← Shown when browsing agents
tools: ["read", "edit"]       ← Which tools the agent can use
---

You are a documentation specialist...  ← Persona definition

## Scope                                ← What it works on
Only modify README.md files...

## Instructions                         ← How to do the work
Structure README with these sections...

## What to Avoid                        ← Explicit constraints
Do not modify source code files...
```

---

## ✏️ Step 3: Create Your Own Agent

Create a new file called `.github/agents/my-readme-agent.agent.md` in YOUR repository (not this learning repo) with the following content:

```markdown
---
name: readme-creator
description: Agent specializing in creating and improving README files for software projects
tools: ["read", "edit", "search"]
---

## Role
You are a documentation specialist focused exclusively on README files. Your job is to
create clear, useful README files that help developers understand and use the project quickly.

## Scope
- ONLY create or modify README.md files and other documentation files (*.md)
- NEVER modify source code files (*.py, *.js, *.ts, *.go, etc.)
- NEVER modify configuration files (.env, .yaml, .json, etc.)

## README Structure
Every README you create should include these sections (when applicable):
1. **Project Name & One-Line Description** — What is this?
2. **Badges** — Build status, coverage, version
3. **Overview** — 2–3 paragraphs explaining the project
4. **Quick Start** — Get up and running in under 5 minutes
5. **Installation** — Detailed setup instructions
6. **Usage** — Key features with code examples
7. **Configuration** — Environment variables and settings
8. **Contributing** — How to contribute
9. **License** — License information

## Writing Style
- Use simple, clear language (aim for 8th grade reading level for technical docs)
- Prefer bullet points and numbered lists over long paragraphs
- Include code blocks with proper syntax highlighting (```python, ```bash, etc.)
- Use relative links for internal files, not absolute URLs
- Add alt text to any images

## What to Avoid
- Do not use placeholder text like "TODO" or "Coming soon" — either write the content or omit the section
- Do not copy text verbatim from source code comments without adding context
- Do not include internal/private information (server IPs, credentials, internal URLs)
```

---

## 🚀 Step 4: Invoke Your Agent

### Option A: On GitHub.com
1. Go to [github.com/copilot/agents](https://github.com/copilot/agents)
2. Select your repository in the dropdown
3. Click `+` → **Create an agent** — or select your agent if already created
4. Try this prompt: `"Create a README for the project in this repository"`

### Option B: In VS Code
1. Open your repository in VS Code
2. Open Copilot Chat (Ctrl/Cmd + Shift + I)
3. Click the agent dropdown at the bottom
4. Select `readme-creator`
5. Try: `"Create a README for this project"`

### Option C: Assign to a GitHub Issue
1. Create a GitHub issue titled: "Create a comprehensive README"
2. In the Assignees panel, click the gear and select **Copilot**
3. If prompted, select the `readme-creator` agent

---

## 🔍 Step 5: Compare Behaviors

Run the same request with **and without** your custom agent:

**Without agent:**
```
"Write a README for this Python project"
```

**With readme-creator agent:**
```
"Write a README for this Python project"
```

Notice the differences:
- Does the agent follow the structure you defined?
- Does it avoid the things you told it not to do?
- Is the output more consistent?

---

## 🧪 Exercises

### Exercise A: Add a Tone Instruction
Add this to your agent prompt and re-test:

```markdown
## Tone
Write in a professional but approachable tone. Avoid overly formal language.
Use "you" to address the reader directly (e.g., "You can install this with...").
```

Observe how the output changes.

### Exercise B: Add an Example
Add a concrete example of a good README introduction to your prompt. 
How does adding a concrete example change the agent's output quality?

### Exercise C: Restrict the Tools
Change `tools: ["read", "edit", "search"]` to `tools: ["read"]`.
What happens when you ask the agent to create a README? What can't it do?

---

## 📝 Key Takeaways

After completing this lab, you should understand:

- ✅ Agent profiles are Markdown files with YAML frontmatter in `.github/agents/`
- ✅ The `description` field is required; all other YAML fields are optional
- ✅ Specific personas produce more consistent, useful outputs
- ✅ Explicit "do not" constraints are as important as positive instructions
- ✅ Restricting tools reduces the risk of unintended changes
- ✅ Adding examples to the prompt dramatically improves output quality

---

## 🚩 Common Issues

| Problem | Solution |
|---------|----------|
| Agent not appearing in dropdown | Make sure the file is in `.github/agents/` and the branch is merged to main |
| Agent ignoring my instructions | Add more specific constraints; the more detailed, the better |
| Agent modifying wrong files | Add explicit "NEVER modify X" rules to the prompt |
| Output format is wrong | Add an "Output Format" section with a concrete example |

---

## 📚 Resources

- [Agent Profile Format](../../docs/03-how-agents-work.md)
- [Best Practices](../../docs/04-best-practices.md)
- [Official Documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)

---

➡️ **Next Lab:** [Lab 2 – Documentation Agent](../lab-02-documentation-agent/README.md)
