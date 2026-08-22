# Season 1 • Day 10

## Today's Scene

At 5:41 p.m., a storm presses hard against the ferry terminal windows. Mara is closing the shift when the maintenance supervisor calls from the dock. The hydraulic-warning note, note 1, has been resolved. The valve was repaired, the inspection passed, and leaving the warning in Harbor would send the night crew looking for a danger that is no longer there.

Joel reaches for the delete command. Beside note 1 sits note 2: the fuel manifest the morning crew still needs. Mara points to the handoff board. “Remove the resolved warning,” she says, “not a note that happens to be nearby.” Harbor must act on the one number it was given and leave every other record in place.

Then Joel notices the empty space note 1 will leave. “Will the next note become note 1?” he asks. Mara shakes her head. That number belonged to a real warning and a real decision. Reusing it would make an old handoff card point to a different event. A deleted note may be gone, but its identifier must not be handed to another note as though the history never existed.

Stewardship keeps what matters in proper order, even when clearing away what is finished.

---

## Scripture

Genesis 2:15

---

## Formation

Stewardship

---

## Engineering Principle

Let the database assign durable identifiers so deleting a resource cannot make its identifier mean something new later.

---

## Technical Source

SQLite documentation - AUTOINCREMENT: https://www.sqlite.org/autoinc.html

---

## Today's Build

In `src/harbor.py`, implement safe deletion of one note with `DELETE /notes/<int:note_id>`. Ensure a fresh Harbor database creates `notes.id` as `INTEGER PRIMARY KEY AUTOINCREMENT`, and change valid note creation to use the identifier SQLite assigns rather than calculating one. Delete only the note matching `note_id`. When that note exists, return HTTP status `204` with an empty response body. When it does not exist, return HTTP status `404` and JSON exactly `{"error": "Note not found."}`. A later valid `POST /notes` must receive a new, never-before-used identifier.

---

## Technical Deliverables

☐ Create fresh Harbor databases with `notes.id` as an `INTEGER PRIMARY KEY AUTOINCREMENT` column, and use SQLite's generated identifier for each valid `POST /notes` response.

☐ Add one `DELETE /notes/<int:note_id>` route that deletes only the row whose `id` matches the requested identifier.

☐ Return the specified `204` response for a deleted note and the specified `404` response for a missing note, leaving every other note unchanged.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, use a fresh `data/harbor.sqlite3` database for this exercise. With Harbor running, create two notes through the existing valid `POST /notes` endpoint: `{"text":"Hydraulic warning cleared; inspect valve at noon"}` and `{"text":"Fuel manifest sent to the morning crew"}`. The responses identify them as notes `1` and `2`. Then run `curl -i -X DELETE http://127.0.0.1:5000/notes/1`. It returns HTTP status `204` with an empty response body. `curl -i http://127.0.0.1:5000/notes/1` returns HTTP status `404` and a body that parses to exactly `{"error": "Note not found."}`. `curl -i http://127.0.0.1:5000/notes` returns HTTP status `200` and a body that parses to exactly `{"notes": [{"id": 2, "text": "Fuel manifest sent to the morning crew"}]}`. Then `curl -i -X POST http://127.0.0.1:5000/notes -H 'Content-Type: application/json' -d '{"text":"Storm-gate inspection scheduled for midnight"}'` returns HTTP status `201` and a body that parses to exactly `{"note": {"id": 3, "text": "Storm-gate inspection scheduled for midnight"}}`. `curl -i -X DELETE http://127.0.0.1:5000/notes/999` returns HTTP status `404` and a body that parses to exactly `{"error": "Note not found."}`. Harbor still has no authentication, no frontend, and no automated tests.

---

## Tomorrow Depends On

Tomorrow depends on Harbor removing one identified note safely before it can handle errors intentionally.

---

## My Reflection

What finished responsibility might you be tempted to discard carelessly, rather than conclude in a way that protects the people who depend on its history?

When transitioning from serving a church, working a job, or moving on from a relationship. If any of these responsibilities have become frustrating and have reached their natural conclusion, it can be tempting to discard these relationships and walk away carelessly.