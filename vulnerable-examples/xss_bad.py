def render_comment(comment):
    # This function is vulnerable to XSS attacks because it directly renders user input without sanitization.
    return f"<div class='comment'>{comment}</div>"

if __name__ == "__main__":
    payload = "<script>alert(1)</script>"
    print(render_comment(payload))
