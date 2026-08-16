# Season 1 • Day 4

## Today's Scene

Mara is back on call before sunrise. The incident is not dramatic yet, which is exactly why the note matters. A database replica is lagging, a customer report is unclear, and the next engineer will need the latest known fact without reading thirty lines of chat.

Yesterday, Harbor could show an empty shelf: `{"notes": []}`. Today, Mara needs to place the first note on that shelf.

The team almost makes the moment too large. One engineer wants note titles, authors, timestamps, tags, priorities, and links to incident IDs. Another wants a database migration before Harbor accepts anything. Someone suggests returning only `{"ok": true}` from the create request because it is faster.

Then Mara asks the question that exposes the responsibility: "If I hand Harbor a note, how do I know which note it accepted?"

A create endpoint is not a shrug at the door. It receives something on behalf of another person. It should accept one clear shape, create one resource, and return the thing it created with an identifier Mara can use again. Not every future feature. Not permanent storage yet. A receipt.

Today, Harbor becomes responsible for the first note it accepts.

---

## Scripture

Luke 12:48

---

## Formation

Responsibility

---

## Engineering Principle

A create endpoint should accept one clear representation and return the created resource with a stable identifier.

---

## Technical Source

MDN Web Docs - POST request method: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST

---

## Today's Build

Add note creation to `src/harbor.py` by making `POST /notes` accept valid JSON exactly shaped as `{"text": "<note text>"}`, create an in-memory note with an integer `id` starting at `1`, return HTTP status `201`, and return the created note as JSON exactly shaped as `{"note": {"id": 1, "text": "<note text>"}}` for the first created note.

---

## Technical Deliverables

☐ Keep the existing `GET /health` route unchanged.

☐ Keep `GET /notes` returning HTTP status `200` and make it return the in-memory notes collection after notes are created.

☐ Add `POST /notes` so a valid JSON request body with exactly one top-level string field, `text`, creates a note with a stable integer `id` and returns the created note with HTTP status `201`.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, `uv run flask --app src.harbor routes` shows `/health` and `/notes`, with `/notes` accepting both `GET` and `POST`. With Harbor running, `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '{"text":"Replica lag is still under review"}'` returns HTTP status `201`, a JSON response, and a body that parses to exactly `{"note": {"id": 1, "text": "Replica lag is still under review"}}` when it is the first created note in the current process. A later `curl -i http://127.0.0.1:5000/notes` returns HTTP status `200` and JSON exactly equal to `{"notes": [{"id": 1, "text": "Replica lag is still under review"}]}`. Harbor still has no SQLite persistence, no input validation for malformed requests, no read-one route, no update route, no delete route, no authentication, and no frontend.

---

## Tomorrow Depends On

Tomorrow depends on Harbor creating notes in memory before those notes are moved into durable storage.

---

## My Reflection

Where are you tempted to receive responsibility without giving the person you serve a clear receipt for what you accepted?

Fatherhood, because it's a daily responsibility and requires a lot it's easy to receive the responsibility without serving a clear receipt for what I accepted.