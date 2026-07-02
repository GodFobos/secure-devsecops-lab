from app.main import app


def test_security_headers_are_set():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers['X-Content-Type-Options'] == 'nosniff'
    assert response.headers['X-Frame-Options'] == 'SAMEORIGIN'
    assert response.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"
