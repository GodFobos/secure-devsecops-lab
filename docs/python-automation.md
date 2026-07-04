# Python Automation

## Goal

This project uses Python not only for the Flask app, but also for security and DevOps automation.

## Planned scripts

```text
automation/
├── repo_audit.py
├── secret_scan.py
├── workflow_audit.py
├── healthcheck.py
└── security_headers_check.py
```

## Why automation matters

Manual security checks are easy to forget.

Automation helps enforce repeatable checks in CI/CD:

- repository audit;
- secret detection;
- dependency audit;
- workflow security review;
- healthcheck;
- security headers check.

## First automation target

The first planned automation script is:

```text
automation/repo_audit.py
```

It will check repository structure and report missing expected files.
