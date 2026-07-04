def render_comment(comment: str) -> str:
    # This function takes a comment string as input and returns an HTML div element containing the comment.
    return f"<div>{comment}</div>"

if __name__ == "__main__":
    payload = "<script>alert(1)</script>"
    print(render_comment(payload))
