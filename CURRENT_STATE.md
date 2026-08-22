# Current State

Version: 0.1

---

## Season 0

Theme:

Working as Worship

Total Days:

7

Current Day:

Complete after Day 6

Final Artifact:

A polished command-line application that faithfully serves one real person.

Formation Outcome:

The reader understands that software development can become an act of faithful service to Christ.

Engineering Outcome:

The reader can create small, useful software that clearly serves one person's need.

Current Application:

A polished command-line program at `src/serve_one_person.py` that reads Ruth's repeated requirement from `data/ruth_requirement.json` by default, accepts an injected data file path for tests, validates required saved fields before formatting, protects both the exact success sentence and the expected validation failure with automated tests, prints success to standard output, prints expected validation errors to standard error without a traceback, and exits with an understandable status code at the command boundary.

---

## Season 1

Theme:

Building Something That Works

Total Days:

14

Current Day:

Ready for Day 11

Final Artifact:

Harbor v1, a small complete HTTP API for creating, retrieving, updating, listing, and deleting notes.

Formation Outcome:

The reader becomes a careful builder who listens before assuming, chooses deliberately, verifies work, and remembers the person being served.

Engineering Outcome:

The reader understands how a human need moves through requirement, HTTP request, application logic, persistence, response, and verification.

Current Application:

After Day 10, Harbor is defined by one requirement artifact at `data/harbor_need.json` with exactly three top-level string fields: `user`, `need`, and `success`, and one minimal Flask application at `src/harbor.py`. The Flask app has an application object named `app`, keeps `GET /health` returning HTTP status `200` and JSON where `service` is `harbor` and `status` is `ok`, keeps `GET /notes` returning HTTP status `200`, keeps valid `POST /notes` returning HTTP status `201`, keeps valid `PATCH /notes/<int:note_id>` returning HTTP status `200`, keeps `DELETE /notes/<int:note_id>` returning HTTP status `204` when it deletes a note, and uses Python's built-in `sqlite3` module to persist notes in a local SQLite database at `data/harbor.sqlite3`. Harbor creates a `notes` table when needed with `id INTEGER PRIMARY KEY AUTOINCREMENT` and required text value `text`. `POST /notes` and `PATCH /notes/<int:note_id>` use Flask's default `request.get_json()` behavior: an unsupported media type receives HTTP status `415` and malformed JSON receives HTTP status `400`. After Flask parses JSON, each route accepts only an object exactly shaped as `{"text": "<note text>"}`. `POST /notes` inserts only the text into SQLite, returns the created note as JSON shaped as `{"note": {"id": <new id>, "text": "<note text>"}}`, and uses the identifier SQLite assigns, with `id` starting at `1` in a fresh database. A created identifier is never reused: after deleting note `1` from notes `1` and `2`, the next valid `POST /notes` returns note `3`. `PATCH /notes/<int:note_id>` queries for exactly the requested positive integer identifier; when it exists, it updates only that note's `text` and returns HTTP status `200` with JSON shaped as `{"note": {"id": <id>, "text": "<updated text>"}}`; when it does not, it returns HTTP status `404` and JSON exactly `{"error": "Note not found."}`. Every other parsed JSON value receives HTTP status `400` and JSON exactly `{"error": "Request body must be a JSON object with exactly one string field, text."}`; every rejected request leaves the persisted notes unchanged. `GET /notes` reads notes from SQLite in ascending `id` order and returns JSON shaped as `{"notes": [{"id": 1, "text": "<note text>"}]}`. `GET /notes/<int:note_id>` queries for exactly the requested positive integer identifier, returns HTTP status `200` and JSON shaped as `{"note": {"id": <id>, "text": "<text>"}}` when the note exists, and returns HTTP status `404` and JSON exactly `{"error": "Note not found."}` when it does not. `DELETE /notes/<int:note_id>` deletes only the note matching the requested identifier and returns HTTP status `204` with an empty response body; if no note matches, it returns HTTP status `404` and JSON exactly `{"error": "Note not found."}`, without changing persisted notes. Created notes survive a Flask process restart. SQLite connections that read note rows return `sqlite3.Row` objects, and one function named `note_from_row` is the canonical translation from a SQLite note row to the API note dictionary with `id` and `text`; `GET /notes`, `GET /notes/<int:note_id>`, successful `POST /notes`, and successful `PATCH /notes/<int:note_id>` use it for note responses. Harbor does not authenticate users, serve a frontend, or have automated tests.

Next Lesson:

Season 1 Day 11 - Humility - Handle errors intentionally.

Question:

How can Harbor give callers a consistent, intentional JSON response when Flask or SQLite raises an unexpected error?

Engineering Principle:

Translate unexpected internal failures into one deliberate API response rather than exposing implementation details.

Formation:

Humility

Primary Source:

Flask documentation - Error Handling: https://flask.palletsprojects.com/en/stable/errorhandling/
