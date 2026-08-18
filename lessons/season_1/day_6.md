# Season 1 • Day 6

## Today's Scene

At 3:11 a.m., Mara opens Harbor after the pager settles and reads the note she left an hour earlier: "Replica lag recovered after cache warmup; watch checkout errors." The note is there. The identifier is there. For one quiet minute, the system seems trustworthy.

Then Joel points at the code during the handoff. `POST /notes` builds its response from the request and a generated identifier. `GET /notes` builds the same-looking response by counting positions in a SQLite result: first value, second value. They agree today, but only by coincidence. A small query change—selecting `text` before `id`, or adding a column later—could make Harbor confidently label a sentence as an identifier. No alarm would sound. The API would simply tell the next engineer the wrong thing.

Mara does not propose an object hierarchy or a new framework. She asks one narrower question: "Where does Harbor decide what a note is?" The team chooses one answer. Every database row that becomes an API note will pass through one deliberate translation. The database can keep its rows; Harbor will present one stable note shape to the person depending on it.

Wisdom is not adding more structure than the work needs. It is seeing the one decision already being made in two places and making it once, on purpose.

---

## Scripture

Proverbs 24:3

---

## Formation

Wisdom

---

## Engineering Principle

As behavior grows, define one canonical data representation instead of scattering shape decisions across routes.

---

## Technical Source

Python documentation - sqlite3 row_factory: https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory

---

## Today's Build

In `src/harbor.py`, establish one canonical API representation for a note from a SQLite row: make the SQLite connections that read notes use `sqlite3.Row`, add one function named `note_from_row` that returns exactly `{"id": <row id>, "text": "<row text>"}`, and use that function for the note returned by both `GET /notes` and `POST /notes`. After inserting a valid note, `POST /notes` must read that created row by its inserted identifier before returning it. Do not add fields, routes, input validation, authentication, or a frontend.

---

## Technical Deliverables

☐ Keep `GET /health` unchanged and keep the existing `GET /notes` and valid `POST /notes` HTTP statuses and JSON response envelopes unchanged.

☐ Configure every SQLite connection that reads note rows for `GET /notes` or `POST /notes` to return `sqlite3.Row` objects, so `note_from_row` accesses the `id` and `text` columns by name.

☐ Use the single `note_from_row` function to form every note dictionary returned from SQLite by `GET /notes` and by the successful `POST /notes` response.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, use a fresh `data/harbor.sqlite3` database for this exercise. In `src/harbor.py`, exactly one function named `note_from_row` converts a SQLite note row into the API note dictionary, and both `get_notes` and `create_note` call it. With Harbor running, `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '{"text":"Replica lag recovered after cache warmup"}'` returns HTTP status `201`, a JSON response, and a body that parses to exactly `{"note": {"id": 1, "text": "Replica lag recovered after cache warmup"}}`. A later `curl -i http://127.0.0.1:5000/notes` returns HTTP status `200` and JSON exactly equal to `{"notes": [{"id": 1, "text": "Replica lag recovered after cache warmup"}]}`. Harbor still has no input validation for malformed requests, no read-one route, no update route, no delete route, no authentication, and no frontend.

---

## Tomorrow Depends On

Tomorrow depends on Harbor using one deliberate note representation before it decides which incoming requests are safe to persist.

---

## My Reflection

Where are you treating an accidental agreement as wisdom instead of pausing to define clearly what you have been entrusted to carry?

Everyday I encounter these accidental agreements via cultural norms and unspoken rules. Time is a simple one, I am a steward of God's time for my life and I encounter many daily obstacles wanting to trade my time for something. When I step back and cleary define that the time God has entrusted me with is my to stewart wisely I no longer want to engage in things that use that time unwisely because it assumes I accidentally agree with it.