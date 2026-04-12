---
engine: copilot
imports:
  - githubnext/agentics/workflows/ci-doctor.md@main
on:
  workflow_run:
    workflows: ["Code Quality", "Python Tests"]
    types: [completed]
    branches: [main]
if: ${{ github.event.workflow_run.conclusion == 'failure' || github.event.workflow_run.conclusion == 'cancelled' }}
---

# CI Doctor

Imported from upstream agentics.
