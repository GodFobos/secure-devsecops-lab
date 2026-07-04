import html

def render_comment(comment: str) -> str:
    # This function takes a comment string as input and returns an HTML div element containing the comment.
    # It uses html.escape to prevent XSS attacks by escaping special characters in the comment.
    safe_comment = html.escape(comment)
    return f"<div>{safe_comment}</div>"

if __name__ == "__main__":
    payload = "<script>alert(1)</script>"
    print(render_comment(payload))
