from flask import Flask
from flask import request

app = Flask(__name__)

notes = []

@app.route("/health")
def health():
    return {"service": "harbor", "status": "ok"}, 200

@app.get("/notes")
def get_notes():
    return {"notes": notes}, 200

@app.post("/notes")
def create_note():
    data = request.get_json()

    note = {
        "id": len(notes) + 1,
        "text": data["text"]
    }

    notes.append(note)

    return {"note": note}, 201

