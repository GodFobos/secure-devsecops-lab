from flask import Flask, jsonify, request # pyright: ignore[reportMissingImports]
import html

app = Flask(__name__)
NOTES = []


@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

@app.get('/')
def index():
    return jsonify(
        {
            "service": "Secure DevSecOps Lab",
            "status": "running"
        }
    )

@app.get('/health')
def health():
    return jsonify(
        {
            "status": "ok"
        }
    )


@app.get("/version")
def version():
    return jsonify({
        "version": "0.1.0"
    })


@app.get("/notes")
def list_notes():
    return jsonify({
        "notes": NOTES
    })


@app.post("/notes")
def create_note():
    data = request.get_json(silent=True)
    raw_text = data.get("text", "")
    safe_text = html.escape(raw_text)

    note = {
        "id": len(NOTES) + 1,
        "text": safe_text
    }

    NOTES.append(note)
    return jsonify(note), 201

if __name__ == "__main__":
    app.run(debug=False)
