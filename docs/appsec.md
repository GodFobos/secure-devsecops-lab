# AppSec Notes

## Current focus

This project is a small AppSec and DevSecOps training lab.

The current application has one important user input point:

```text
POST /notes
```

Because of that, the first relevant AppSec topic is XSS.

## XSS

Cross-Site Scripting happens when user-controlled input is rendered as executable HTML or JavaScript.

Bad pattern:

```python
def render_comment(comment: str) -> str:
    return f"<div>{comment}</div>"
```

If the user sends this value:

```html
<script>alert(1)</script>
```

the browser may execute it as JavaScript.

## Safer pattern

```python
import html

def render_comment_safe(comment: str) -> str:
    return f"<div>{html.escape(comment)}</div>"
```

## Current protection in the app

The `/notes` endpoint escapes user input before storing it:

```python
safe_text = html.escape(raw_text)
```

## Security headers

The Flask app currently sets basic security headers:

- `X-Content-Type-Options`
- `X-Frame-Options`
- `Referrer-Policy`
