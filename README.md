# Versioning

## Add branch protection rules

```bash
gh api --method PUT /repos/ricky-lim/versioning/branches/main/protection --input branch-protection-rules.json
```