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

Ready for Day 7

Final Artifact:

Harbor v1, a small complete HTTP API for creating, retrieving, updating, listing, and deleting notes.

Formation Outcome:

The reader becomes a careful builder who listens before assuming, chooses deliberately, verifies work, and remembers the person being served.

Engineering Outcome:

The reader understands how a human need moves through requirement, HTTP request, application logic, persistence, response, and verification.

Current Application:

After Day 6, Harbor is defined by one requirement artifact at `data/harbor_need.json` with exactly three top-level string fields: `user`, `need`, and `success`, and one minimal Flask application at `src/harbor.py`. The Flask app has an application object named `app`, keeps `GET /health` returning HTTP status `200` and JSON where `service` is `harbor` and `status` is `ok`, keeps `GET /notes` returning HTTP status `200`, keeps `POST /notes` returning HTTP status `201`, and uses Python's built-in `sqlite3` module to persist notes in a local SQLite database at `data/harbor.sqlite3`. Harbor creates a `notes` table when needed with an integer primary key `id` and required text value `text`. `POST /notes` accepts valid JSON exactly shaped as `{"text": "<note text>"}`, inserts the note into SQLite, and returns the created note as JSON shaped as `{"note": {"id": <new id>, "text": "<note text>"}}`, with `id` starting at `1` in a fresh database. `GET /notes` reads notes from SQLite in ascending `id` order and returns JSON shaped as `{"notes": [{"id": 1, "text": "<note text>"}]}`. Created notes survive a Flask process restart. SQLite connections that read note rows return `sqlite3.Row` objects, and one function named `note_from_row` is the canonical translation from a SQLite note row to the API note dictionary with `id` and `text`; both `GET /notes` and successful `POST /notes` use it. Harbor does not validate malformed input, read one note, update one note, delete one note, authenticate users, or serve a frontend.

Next Lesson:

Season 1 Day 7 - Integrity - Validate malformed create requests.

Question:

How can Harbor reject malformed create requests before they become persisted notes?

Engineering Principle:

Validate external input at the application boundary before it reaches durable state.

Formation:

Integrity

Primary Source:

Flask documentation - Request.get_json: https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_json

### Deferred Curriculum Guardrail

Day 10 must prove that deleting a note does not cause a later `POST /notes` to reuse an existing identifier. After deleting ID 1 from notes 1 and 2, the next created note must have ID 3. (Delete this after day 10)