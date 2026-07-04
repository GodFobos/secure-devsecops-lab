# Git Notes

## Basic model

Git tracks changes through several states:

```text
working directory -> staging area -> commit -> remote repository
```

## Key commands

```bash
git status
git add .
git commit -m "message"
git log --oneline
git branch
git switch -c feature/name
git push
git pull
```

## Branch workflow

The project uses GitHub Flow:

```text
feature branch -> pull request -> merge into main
```

## Rules

- Do not work directly in `main`.
- Create a feature branch for each logical change.
- Commit small and meaningful changes.
- Open a Pull Request before merging into `main`.
- Run tests before pushing.
