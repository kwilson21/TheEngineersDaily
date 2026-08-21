# Season 1 • Day 9

## Today's Scene

At 8:03 a.m., Mara is standing beside the ferry terminal's backup generator when the night engineer radios in. The hydraulic-warning note is still open, but its wording is now misleading: the valve has been inspected, and the crew needs the note to say what remains. The handoff card names note 1. A different note, note 2, contains the fuel manifest for the morning crew.

Joel suggests adding a new note with the correction. Mara shakes her head. Two notes about one warning would leave the next crew deciding which version to trust. Then he reaches for a broad update that would replace every matching phrase. Mara stops him again. The fuel manifest must remain exactly as it is; the request is to change note 1, not whatever happens to sound related.

They settle on a plain responsibility: Harbor must receive the identifier, find that one stored note, and replace only its text. If the numbered note is absent, it must say so and leave every note untouched. The number on the handoff card is not decoration. It names the work Harbor is responsible to do—and the work it must refuse to do.

Responsibility begins by being clear about what has been entrusted to you, then acting only within that boundary.

---

## Scripture

Romans 14:12

---

## Formation

Responsibility

---

## Engineering Principle

Make a change target explicit before applying it so an update affects only the intended resource.

---

## Technical Source

Flask documentation - HTTP Methods: https://flask.palletsprojects.com/en/stable/quickstart/#http-methods

---

## Today's Build

In `src/harbor.py`, add `PATCH /notes/<int:note_id>`. Use Flask's `note_id` to find exactly that note in `data/harbor.sqlite3`. Use Flask's default `request.get_json()` behavior. After Flask parses JSON, accept only an object exactly shaped as `{"text": "<note text>"}`. For a valid body and an existing note, update only that note's `text` and return HTTP status `200` with JSON exactly `{"note": {"id": <id>, "text": "<updated text>"}}` using `note_from_row`. For every other parsed JSON value, return HTTP status `400` and JSON exactly `{"error": "Request body must be a JSON object with exactly one string field, text."}`. For a valid body and a missing note, return HTTP status `404` and JSON exactly `{"error": "Note not found."}`. Every rejected request must leave persisted notes unchanged.

---

## Technical Deliverables

☐ Add one `PATCH /notes/<int:note_id>` route that receives the target identifier as an integer through Flask's URL converter.

☐ Accept only the specified JSON body, find the note by that identifier, and update only its `text` when the note exists.

☐ Return the specified `200`, `400`, and `404` responses, with every rejected request leaving the database unchanged.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, use a fresh `data/harbor.sqlite3` database for this exercise. With Harbor running, create two notes through the existing valid `POST /notes` endpoint: `{"text":"Hydraulic warning cleared after valve inspection"}` and `{"text":"Fuel manifest sent to the morning crew"}`. Then run `curl -i -X PATCH http://127.0.0.1:5000/notes/1 -H 'Content-Type: application/json' -d '{"text":"Hydraulic warning cleared; inspect valve at noon"}'`. It returns HTTP status `200` and a body that parses to exactly `{"note": {"id": 1, "text": "Hydraulic warning cleared; inspect valve at noon"}}`. `curl -i http://127.0.0.1:5000/notes/2` returns HTTP status `200` and a body that parses to exactly `{"note": {"id": 2, "text": "Fuel manifest sent to the morning crew"}}`. `curl -i -X PATCH http://127.0.0.1:5000/notes/2 -H 'Content-Type: application/json' -d '{"text":2}'` returns HTTP status `400` and a body that parses to exactly `{"error": "Request body must be a JSON object with exactly one string field, text."}`. `curl -i -X PATCH http://127.0.0.1:5000/notes/999 -H 'Content-Type: application/json' -d '{"text":"No change"}'` returns HTTP status `404` and a body that parses to exactly `{"error": "Note not found."}`. A later `curl -i http://127.0.0.1:5000/notes` returns HTTP status `200` and a body that parses to exactly `{"notes": [{"id": 1, "text": "Hydraulic warning cleared; inspect valve at noon"}, {"id": 2, "text": "Fuel manifest sent to the morning crew"}]}`. Harbor still has no delete route, no authentication, no frontend, and no automated tests.

---

## Tomorrow Depends On

Tomorrow depends on Harbor changing one identified note before it can remove one note safely.

---

## My Reflection

Where has a responsibility been entrusted to you that you need to name more precisely before you act?

My responsibility to God, my kids, my wife, my career, my finances, my vessel, and the things I own. I need to be clear about what's been entrusted to me so that I can act only within that boundary.