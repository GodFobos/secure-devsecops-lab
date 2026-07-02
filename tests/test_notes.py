from app.main import app

def test_create_note_escapes_html():
    client = app.test_client()

    response = client.post("/notes", json={
        "text": "<script>alert('XSS');</script>"
    })

    data = response.get_json()

    assert response.status_code == 201
    assert "<script>" not in data["text"]
    assert "&lt;script&gt;" in data["text"]



def test_list_notes_returns_notes_key():
    client = app.test_client()

    response = client.get("/notes")

    data = response.get_json()

    assert response.status_code == 200
    assert "notes" in data
