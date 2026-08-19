# Season 1 • Day 7

## Today's Scene

At 6:42 a.m., Mara is leaving the night shift when a tired engineer sends a request to Harbor with a browser form instead of JSON. Flask answers at once: Harbor accepts JSON here, not a form. A minute later, an automated script sends a JSON array. Then another sends `text` alongside an extra field no one agreed to keep.

Each request reaches the same small door: `POST /notes`. Behind that door is the SQLite file that holds the notes Mara entrusted to Harbor overnight. Flask already guards the HTTP promise: the request must identify itself as JSON, and the JSON must parse. Harbor still owns the next promise: a parsed value must be one object with one string field named `text`.

One engineer suggests storing whatever arrives and fixing it later. Mara pictures the next shift opening a note whose shape nobody can explain. Repairing a bad record would cost more than refusing a bad request while its sender can still correct it.

So the team keeps one plain boundary. Flask continues to name protocol failures with its standard HTTP responses. Harbor names only the shape it owns: one JSON object with one string field named `text`. If a parsed JSON value is not that, Harbor returns one clear answer and changes nothing durable. Integrity is not suspicion of people. It is making the promise at the door match the care taken behind it.

---

## Scripture

Proverbs 10:9

---

## Formation

Integrity

---

## Engineering Principle

Validate each part of external input at the layer that owns its contract.

---

## Technical Source

Flask documentation - Request.get_json: https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_json

---

## Today's Build

In `src/harbor.py`, keep using `request.get_json()` with its default behavior so Flask continues to return HTTP status `415` for an unsupported media type and HTTP status `400` for malformed JSON. After Flask successfully parses JSON, make `POST /notes` accept only an object exactly shaped as `{"text": "<note text>"}`, where `text` is a string. For every other parsed JSON value, return HTTP status `400` with JSON exactly `{"error": "Request body must be a JSON object with exactly one string field, text."}` and do not insert a note into `data/harbor.sqlite3`. Keep valid creates unchanged.

---

## Technical Deliverables

☐ Keep `GET /health`, `GET /notes`, and the successful `POST /notes` status codes and response envelopes unchanged.

☐ Preserve Flask's default responses for a non-JSON content type (`415`) and malformed JSON (`400`) without replacing either response body.

☐ Make `POST /notes` reject a parsed non-object JSON value, a missing `text` field, an extra top-level field, and a non-string `text` value with the one specified HTTP `400` JSON response.

☐ Ensure every rejected create request leaves the persisted `notes` table unchanged.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, use a fresh `data/harbor.sqlite3` database for this exercise. With Harbor running, `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '{"text":"Replica lag recovered after cache warmup"}'` returns HTTP status `201` and a body that parses to exactly `{"note": {"id": 1, "text": "Replica lag recovered after cache warmup"}}`. `curl -i -X POST http://127.0.0.1:5000/notes -d '{"text":"valid"}'` returns Flask's default HTTP status `415`, and `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '{"text":'` returns Flask's default HTTP status `400`. Each of these requests returns HTTP status `400` and a body that parses to exactly `{"error": "Request body must be a JSON object with exactly one string field, text."}`: `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '["text"]'`; `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '{"body":"missing text"}'`; `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '{"text":"valid","author":"Mara"}'`; and `curl -i -X POST http://127.0.0.1:5000/notes -H "Content-Type: application/json" -d '{"text":7}'`. A later `curl -i http://127.0.0.1:5000/notes` returns HTTP status `200` and JSON exactly equal to `{"notes": [{"id": 1, "text": "Replica lag recovered after cache warmup"}]}`. Harbor still has no read-one route, no update route, no delete route, no authentication, no frontend, and no automated tests.

---

## Tomorrow Depends On

Tomorrow depends on Harbor rejecting malformed create requests before it can reliably retrieve one specific persisted note.

---

## My Reflection

Where are you tempted to let an unclear promise pass the door because correcting it early feels uncomfortable?

When applying to a job, my job experience might appear to make me a better fit for one position versus the position that I wanted to apply for. I am tempted to not correct the recruiter because it feels uncomfortable but I cannot let an unclear promise on the job I want to work pass the door.