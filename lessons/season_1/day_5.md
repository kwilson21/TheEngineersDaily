# Season 1 • Day 5

## Today's Scene

Mara writes the note at 2:17 a.m., just after the alert quiets down: "Replica lag recovered after cache warmup; watch checkout errors." It is not poetry. It is better than poetry. It is the one sentence the next engineer needs before making a worse decision in the dark.

Harbor accepts the note. It returns an `id`. Mara exhales.

Then the laptop running the development server restarts.

The room goes still in that particular way engineers recognize. No explosion. No stack trace framed in red. Just absence. `GET /notes` returns an empty collection, and the sentence that should have carried Mara's care into the next hour is gone. The team did not lose the note because the code was malicious. They lost it because memory was treated like a vault when it was only a whiteboard.

Stewardship begins where convenience stops pretending. If Harbor receives something entrusted to it, Harbor should keep it somewhere meant for keeping. Not a cloud platform. Not a queue. Not a grand architecture. A small SQLite database is enough for today's trust.

Today, Harbor learns to keep Mara's notes after the process dies.

---

## Scripture

Genesis 2:15

---

## Formation

Stewardship

---

## Engineering Principle

Important application state should live in durable storage, not only in process memory.

---

## Technical Source

Python documentation - sqlite3: https://docs.python.org/3/library/sqlite3.html

---

## Today's Build

Change Harbor's existing note storage in `src/harbor.py` from an in-memory list to a SQLite database at `data/harbor.sqlite3`, using Python's built-in `sqlite3` module. Create a `notes` table when Harbor needs it, store each note with an integer primary key `id` and required text value `text`, make `POST /notes` insert a valid note into SQLite and return the created note with HTTP status `201`, and make `GET /notes` read notes back from SQLite in ascending `id` order.

---

## Technical Deliverables

☐ Keep the existing `GET /health` route unchanged.

☐ Replace the process-memory `notes` list with SQLite-backed storage in `data/harbor.sqlite3` using one `notes` table with `id` and `text`.

☐ Keep the existing valid `POST /notes` and `GET /notes` response shapes unchanged while making created notes survive a Flask process restart.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, start from no existing `data/harbor.sqlite3` file for this exercise. `uv run flask --app src.harbor routes` still shows `/health` and `/notes`, with `/notes` accepting both `GET` and `POST`. With Harbor running, `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '{"text":"Replica lag recovered after cache warmup"}'` returns HTTP status `201`, a JSON response, and a body that parses to exactly `{"note": {"id": 1, "text": "Replica lag recovered after cache warmup"}}`. After stopping and restarting Harbor, `curl -i http://127.0.0.1:5000/notes` returns HTTP status `200` and JSON exactly equal to `{"notes": [{"id": 1, "text": "Replica lag recovered after cache warmup"}]}`. Harbor still has no input validation for malformed requests, no read-one route, no update route, no delete route, no authentication, and no frontend.

---

## Tomorrow Depends On

Tomorrow depends on Harbor keeping notes in durable storage before the note model becomes more deliberate.

---

## My Reflection

Where are you tempted to treat something entrusted to you as temporary because no one has asked yet what happens after a restart?

Money, although it comes and goes, is it possible to maintain it after a financial restart?