# Secure DevSecOps Lab

Secure DevSecOps Lab is a portfolio project for learning CI/CD, Python automation, AppSec and DevSecOps.

## Current Features

- Minimal Flask application
- Healthcheck endpoint
- Notes endpoint
- Basic output escaping
- Basic security headers
- Pytest tests

## Endpoints

- GET /
- GET /health
- GET /version
- GET /notes
- POST /notes

## Local Development

Create virtual environment:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1


## Project Structure

```text
app/                  Flask application code
tests/                pytest tests
automation/           Python automation scripts
docs/                 technical documentation
scripts/              local and deployment scripts
vulnerable-examples/  AppSec learning examples
.github/              GitHub configuration
```

## Development Workflow

This project uses GitHub Flow:

```text
feature branch -> pull request -> merge into main
```

The `main` branch should remain stable.

All meaningful changes should be developed in a separate feature branch and merged through a Pull Request.
