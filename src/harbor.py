from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)


def setup_db():
    con = sqlite3.connect("data/harbor.sqlite3")
    cur = con.cursor()

    res = cur.execute("SELECT name FROM sqlite_master")

    table_name = res.fetchone()
    if table_name and table_name[0] == "notes":
        cur.close()
        con.close()
        return True
    else:
        res = cur.execute("CREATE TABLE notes(id INTEGER PRIMARY KEY AUTOINCREMENT,text TEXT)")

    cur.close()
    con.close()

setup_db()

def note_from_row(row):
    return {"id": row["id"], "text": row["text"]}

def validate_note_json(data):
    error_str = "Request body must be a JSON object with exactly one string field, text."
    if not isinstance(data, dict):
        raise ValueError(error_str)
    if "text" not in data:
        raise ValueError(error_str)
    if not isinstance(data["text"], str):
        raise ValueError(error_str)
    if len(data.keys()) > 1:
        raise ValueError(error_str)

@app.route("/health")
def health():
    return {"service": "harbor", "status": "ok"}, 200

@app.get("/notes")
def get_notes():
    con = sqlite3.connect("data/harbor.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    res = cur.execute("SELECT * FROM notes ORDER BY id ASC")

    notes = [note_from_row(row) for row in res.fetchall()]

    cur.close()
    con.close()

    return {"notes": notes}, 200

@app.post("/notes")
def create_note():
    data = request.get_json()

    try:
        validate_note_json(data)
    except ValueError as e:
        return {"error": str(e)}, 400

    con = sqlite3.connect("data/harbor.sqlite3")
    con.row_factory = sqlite3.Row

    cur = con.cursor()

    new_note = {
        "text": data["text"]
    }

    cur.execute("INSERT INTO notes(text) VALUES(?)", list(new_note.values()))

    con.commit()

    res = cur.execute("SELECT * FROM notes WHERE id = ?",(cur.lastrowid,))
    row = res.fetchone()
    note = note_from_row(row)

    cur.close()
    con.close()

    return {"note": note}, 201

@app.get("/notes/<int:note_id>")
def get_note(note_id):
    con = sqlite3.connect("data/harbor.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    params = (note_id,)
    res = cur.execute("SELECT * FROM notes WHERE id = ?;", params)

    row = res.fetchone()

    cur.close()
    con.close()

    if not row:
        return {"error": "Note not found."}, 404
    else:
        return {"note": note_from_row(row)}, 200

@app.patch("/notes/<int:note_id>")
def update_note(note_id):
    data = request.get_json()

    try:
        validate_note_json(data)
    except ValueError as e:
        return {"error": str(e)}, 400

    con = sqlite3.connect("data/harbor.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    params = (data["text"], note_id)

    res = cur.execute("UPDATE notes SET text = ? WHERE id = ?", params)
    con.commit()
    res = cur.execute("SELECT * FROM notes WHERE id = ?",(note_id,))
    row = res.fetchone()

    cur.close()
    con.close()

    if not row:
        return {"error": "Note not found."}, 404
    else:
        return {"note": note_from_row(row)}, 200

@app.delete("/notes/<int:note_id>")
def delete_note(note_id):
    con = sqlite3.connect("data/harbor.sqlite3")
    con.row_factory = sqlite3.Row

    cur = con.cursor()

    res = cur.execute("SELECT * FROM notes WHERE id = ?", (note_id,))

    row = res.fetchone()
    if not row:
        cur.close()
        con.close()
        return {"error": "Note not found."}, 404

    res = cur.execute("DELETE FROM notes WHERE id = ?", (note_id,))

    con.commit()

    cur.close()
    con.close()

    return '',204
