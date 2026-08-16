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

Ready for Day 5

Final Artifact:

Harbor v1, a small complete HTTP API for creating, retrieving, updating, listing, and deleting notes.

Formation Outcome:

The reader becomes a careful builder who listens before assuming, chooses deliberately, verifies work, and remembers the person being served.

Engineering Outcome:

The reader understands how a human need moves through requirement, HTTP request, application logic, persistence, response, and verification.

Current Application:

After Day 4, Harbor is defined by one requirement artifact at `data/harbor_need.json` with exactly three top-level string fields: `user`, `need`, and `success`, and one minimal Flask application at `src/harbor.py`. The Flask app has an application object named `app`, keeps `GET /health` returning HTTP status `200` and JSON where `service` is `harbor` and `status` is `ok`, keeps `GET /notes` returning HTTP status `200`, and adds `POST /notes` for creating notes. `POST /notes` accepts valid JSON exactly shaped as `{"text": "<note text>"}`, creates an in-memory note with a stable integer `id` starting at `1`, returns HTTP status `201`, and returns the created note as JSON exactly shaped as `{"note": {"id": 1, "text": "<note text>"}}` for the first created note in the current process. A later `GET /notes` returns the in-memory notes collection as JSON shaped as `{"notes": [{"id": 1, "text": "<note text>"}]}`. Harbor can create and list notes only while the Flask process lives, but does not persist notes, validate malformed input, read one note, update one note, delete one note, authenticate users, or serve a frontend.

Next Lesson:

Season 1 Day 5 - Stewardship - Persist notes with SQLite.

Question:

How can Harbor keep Mara's notes after the Flask process restarts?

Engineering Principle:

Important application state should live in durable storage, not only in process memory.

Formation:

Stewardship

Primary Source:

Python documentation - sqlite3: https://docs.python.org/3/library/sqlite3.html
