# DevSecOps Notes

## Definition

DevSecOps means integrating security controls into the software development and delivery process.

Security should not be a final manual step. It should be part of the pipeline.

## Planned pipeline

```text
feature branch
-> pull request
-> tests
-> secret scan
-> SAST
-> dependency audit
-> workflow audit
-> merge to main
-> staging deployment
-> production approval
```

## Planned checks

- Unit tests with pytest
- Custom secret scanner
- SAST with Semgrep
- Dependency audit with pip-audit
- GitHub Actions workflow audit
- Docker build in GitHub Actions
- Deployment healthcheck
