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
        return True
    else:
        res = cur.execute("CREATE TABLE notes(id INTEGER PRIMARY KEY,text TEXT)")

    cur.close()
    con.close()

setup_db()

def note_from_row(row):
    return {"id": row["id"], "text": row["text"]}

@app.route("/health")
def health():
    return {"service": "harbor", "status": "ok"}, 200

@app.get("/notes")
def get_notes():
    con = sqlite3.connect("data/harbor.sqlite3")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    res = cur.execute("SELECT * FROM notes;")

    notes = [note_from_row(row) for row in res.fetchall()]

    cur.close()
    con.close()

    return {"notes": notes}, 200

@app.post("/notes")
def create_note():
    con = sqlite3.connect("data/harbor.sqlite3")
    con.row_factory = sqlite3.Row
    data = request.get_json()
    cur = con.cursor()
    res = cur.execute("SELECT count(*) FROM notes;")
    count_res = res.fetchone()
    if count_res:
        count = count_res[0]
    else:
        count = 1

    new_note = {
        "id": count + 1,
        "text": data["text"]
    }

    cur.execute("INSERT INTO notes VALUES(?, ?)", list(new_note.values()))

    con.commit()

    res = cur.execute(f"SELECT * FROM notes WHERE id = {count + 1};")
    row = res.fetchone()
    note = note_from_row(row)

    cur.close()
    con.close()

    return {"note": note}, 201

