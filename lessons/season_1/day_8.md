# Season 1 • Day 8

## Today's Scene

At 7:16 a.m., Mara receives a handoff call from the ferry terminal. A crew member remembers that Harbor holds the note about a hydraulic warning, but the terminal has gathered eleven notes since the night shift. Reading the whole list aloud would make the right sentence hard to find, and guessing from the first note would be worse. The crew member has the number from the handoff: note 4.

Joel opens Harbor and sees that the identifier is already stored beside every note. "Then we can just look it up," he says. Mara agrees, but asks what Harbor will say if note 4 is no longer there. A vague empty response would leave the crew guessing whether the request failed, the database was unreachable, or the note simply does not exist. Sending some other note would turn a clear request into a dangerous assumption.

The team gives the request two honest outcomes. When the identifier matches a stored note, Harbor returns that one note in the same deliberate shape it already uses. When it matches nothing, Harbor says so plainly and does not change anything. The small distinction lets the crew decide what to do next with the information they actually have.

Care does not make every answer pleasant. It makes the answer clear enough for the person receiving it to act wisely.

---

## Scripture

Philippians 2:4

---

## Formation

Care

---

## Engineering Principle

Represent the outcome of a lookup explicitly so callers can distinguish a present resource from an absent one.

---

## Technical Source

Flask documentation - Variable Rules: https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules

---

## Today's Build

In `src/harbor.py`, add `GET /notes/<int:note_id>`. Use the positive integer `note_id` supplied by Flask to query `data/harbor.sqlite3` for exactly that note. When a matching row exists, return HTTP status `200` and JSON exactly `{"note": {"id": <id>, "text": "<text>"}}` using the existing `note_from_row` function. When no matching row exists, return HTTP status `404` and JSON exactly `{"error": "Note not found."}`. This route must not insert, update, or delete a note.

---

## Technical Deliverables

☐ Add one `GET /notes/<int:note_id>` route that receives the identifier as an integer through Flask's URL converter.

☐ Query SQLite by that identifier and use `note_from_row` for the successful note response.

☐ Return the specified `200` response for an existing note and the specified `404` response for a missing note without changing persisted notes.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, use a fresh `data/harbor.sqlite3` database for this exercise. With Harbor running, create two notes through the existing valid `POST /notes` endpoint: `{"text":"Hydraulic warning cleared after valve inspection"}` and `{"text":"Fuel manifest sent to the morning crew"}`. `curl -i http://127.0.0.1:5000/notes/1` returns HTTP status `200` and a body that parses to exactly `{"note": {"id": 1, "text": "Hydraulic warning cleared after valve inspection"}}`. `curl -i http://127.0.0.1:5000/notes/999` returns HTTP status `404` and a body that parses to exactly `{"error": "Note not found."}`. A later `curl -i http://127.0.0.1:5000/notes` returns HTTP status `200` and a body that parses to exactly `{"notes": [{"id": 1, "text": "Hydraulic warning cleared after valve inspection"}, {"id": 2, "text": "Fuel manifest sent to the morning crew"}]}`. Harbor still has no update route, no delete route, no authentication, no frontend, and no automated tests.

---

## Tomorrow Depends On

Tomorrow depends on Harbor retrieving one note honestly before it can change one note deliberately.

---

## My Reflection

When a person needs a clear answer from you, where might you be tempted to hide absence or uncertainty instead of naming it truthfully?

When I don't know the answer, normally I say I don't know but when in a situation where I think there may be a chance I could know I may try to remember or find the answer on the spot. In either instance, the more truthful answer is to name that moment truthfully. Either saying "I don't know" or only answering up to my knowledge and resisting the urge to answer beyond that might be ways to resist this temptation or uncertainty.