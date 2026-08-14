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

Ready for Day 3

Final Artifact:

Harbor v1, a small complete HTTP API for creating, retrieving, updating, listing, and deleting notes.

Formation Outcome:

The reader becomes a careful builder who listens before assuming, chooses deliberately, verifies work, and remembers the person being served.

Engineering Outcome:

The reader understands how a human need moves through requirement, HTTP request, application logic, persistence, response, and verification.

Current Application:

After Day 2, Harbor is defined by one requirement artifact at `data/harbor_need.json` with exactly three top-level string fields: `user`, `need`, and `success`, and one minimal Flask application at `src/harbor.py`. The Flask app has an application object named `app`, keeps `GET /health` returning HTTP status `200` and JSON where `service` is `harbor` and `status` is `ok`, and adds one notes collection route, `GET /notes`, which returns HTTP status `501` and JSON where `error` is `notes collection is not implemented yet`. Harbor has a clear URL for Mara's notes collection, but does not store, list, create, read, update, or delete notes yet, and has no persistence.

Next Lesson:

Season 1 Day 3 - Faithfulness - GET a collection of notes.

Question:

What should Mara receive when she asks for all notes before any notes exist?

Engineering Principle:

A collection endpoint should return a predictable representation, even when the collection is empty.

Formation:

Faithfulness

Primary Source:

MDN Web Docs - GET request method: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET
