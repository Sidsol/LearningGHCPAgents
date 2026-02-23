# Agent Profile Examples Library

> Ready-to-use agent profiles for common development workflows. Copy any of these to your project's `.github/agents/` directory and customize to fit your team's needs.

---

## Available Examples

| Agent | Description | Complexity |
|-------|-------------|------------|
| [minimal-agent.agent.md](minimal-agent.agent.md) | A simple README creator — great starting point | Beginner |
| [full-stack-agent.agent.md](full-stack-agent.agent.md) | React/TypeScript + Python/FastAPI development | Intermediate |
| [security-agent.agent.md](security-agent.agent.md) | OWASP-based security scanning and reporting | Intermediate |
| [devops-agent.agent.md](devops-agent.agent.md) | CI/CD pipelines, Docker, Kubernetes, Terraform | Advanced |

---

## How to Use These Examples

1. **Pick the template** closest to your use case
2. **Copy it** to `.github/agents/` in your repository
3. **Customize the prompt** with your team's specific conventions
4. **Test it** on 5–10 real tasks before sharing with the team
5. **Iterate** based on what works and what doesn't

---

## Customization Tips

### Replace Generic Rules with Yours

Every template has placeholder conventions. Replace them:

```diff
- Use TypeScript with React
+ Use TypeScript 5.3 with React 18 and our custom hooks library from src/hooks/
```

### Add Your Stack-Specific Tools

```diff
- tools:
-   - read
-   - edit
+ tools:
+   - read
+   - edit
+   - run_in_terminal  # If the agent needs to run commands
```

### Encode Your "No-Go" Zones

```markdown
## Absolute Constraints
- NEVER modify files in src/core/ — these are owned by the platform team
- NEVER change package.json dependencies without mentioning it in the output
- NEVER create files outside of src/features/ for new feature work
```

---

## Community Resources

Browse thousands of community-contributed agent profiles at **[github/awesome-copilot](https://github.com/github/awesome-copilot)**.

---

↩️ **Back to:** [Repository Overview](../README.md)
