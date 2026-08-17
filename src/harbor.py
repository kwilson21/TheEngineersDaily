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

@app.route("/health")
def health():
    return {"service": "harbor", "status": "ok"}, 200

@app.get("/notes")
def get_notes():
    con = sqlite3.connect("data/harbor.sqlite3")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM notes;")

    notes = [{"id": r[0], "text": r[1]} for r in res.fetchall()]

    cur.close()
    con.close()

    return {"notes": notes}, 200

@app.post("/notes")
def create_note():
    con = sqlite3.connect("data/harbor.sqlite3")
    data = request.get_json()
    cur = con.cursor()
    res = cur.execute("SELECT count(*) FROM notes;")
    count_res = res.fetchone()
    if count_res:
        count = count_res[0]
    else:
        count = 1

    note = {
        "id": count + 1,
        "text": data["text"]
    }

    cur.execute("INSERT INTO notes VALUES(?, ?)", list(note.values()))

    con.commit()

    cur.close()
    con.close()

    return {"note": note}, 201

