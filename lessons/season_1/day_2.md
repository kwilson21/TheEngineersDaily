# Season 1 • Day 2

## Today's Scene

Mara's handoff notes are still living in a scattering of places: one line in the incident channel, one copied command in a terminal buffer, one tense sentence in a call transcript. Harbor can now answer `GET /health`, so the service is reachable, but reachability is not yet usefulness.

The team gathers around the next choice and tries to make it larger than it is. One engineer suggests `/api/v1/incidents/handoffs/notes`. Another wants `/mara/notes`, because Mara is the first user. Someone else proposes `/search`, because searching will matter someday. Each suggestion has a reason, and each reason pulls the system toward a different future.

Then Mara describes the moment she actually cares about. After an alert, she wants her tool to ask one plain place for the notes. Not a maze. Not a prediction of every feature Harbor might have later. Just the shelf where incident notes belong.

Clarity clears the table. The resource is the collection of notes. The URL is `/notes`. Today, Harbor does not need to list them yet, store them yet, or design their shape. It needs to name them truthfully so tomorrow's behavior has a clear place to stand.

---

## Scripture

Matthew 5:37

---

## Formation

Clarity

---

## Engineering Principle

A URL should name one resource clearly before behavior grows around it.

---

## Technical Source

Flask official Quickstart - Routing: https://flask.palletsprojects.com/en/stable/quickstart/#routing

---

## Today's Build

Add exactly one new Harbor route in `src/harbor.py`: `GET /notes`. For today, the route must only reserve the notes collection URL by returning HTTP status `501` and JSON with exactly one string field: `error` set to `notes collection is not implemented yet`.

---

## Technical Deliverables

☐ Keep the existing `GET /health` route unchanged.

☐ Add one new route at exactly `GET /notes`.

☐ Make `GET /notes` return HTTP status `501` and JSON exactly equal to `{"error": "notes collection is not implemented yet"}`.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, `uv run flask --app src.harbor routes` shows both `/health` and `/notes`. `curl -i http://127.0.0.1:5000/notes` returns HTTP status `501`, a JSON response, and a body that parses to exactly `{"error": "notes collection is not implemented yet"}`. Harbor has no note storage, no note schema, no create route, no update route, no delete route, no database code, no authentication, and no frontend.

---

## Tomorrow Depends On

Tomorrow depends on Mara's notes collection having one clear URL before it returns real notes.

---

## My Reflection

Where are you tempted to hide uncertainty behind a complicated name instead of choosing the clearest name for the thing in front of you?

The name of an app or project often times will become more complicated than it has to.