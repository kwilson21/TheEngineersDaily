# Season 1 • Day 3

## Today's Scene

The incident has cooled, but Mara is still at her desk. Her browser has three tabs open: the timeline, the chat, and Harbor's `/notes` URL. Yesterday, the team gave that URL a name. Today, Mara clicks it and receives the truth, but not the kind of truth she can use: `notes collection is not implemented yet`.

No one has lost data, because there is no data yet. No one has broken an alert, because Harbor is still small. But the room feels the quiet danger of a half-built promise. A collection that exists only as a placeholder still leaves Mara guessing whether Harbor knows there are no notes, whether the route failed, whether her script should retry, or whether someone needs to be paged.

Faithfulness does not wait until the system is impressive. It begins with the smallest honest behavior. If Mara asks for all notes before any notes exist, Harbor should answer consistently: the request succeeded, and the collection is empty.

So the team resists the urge to invent storage, sample data, note IDs, or a database. They replace the placeholder with one dependable representation. The shelf is empty, but the shelf is real.

---

## Scripture

Luke 16:10

---

## Formation

Faithfulness

---

## Engineering Principle

A collection endpoint should return a predictable representation, even when the collection is empty.

---

## Technical Source

MDN Web Docs - GET request method: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET

---

## Today's Build

Change the existing `GET /notes` route in `src/harbor.py` so it returns HTTP status `200` and JSON exactly equal to `{"notes": []}` when no notes exist. Do not add note storage, sample notes, note IDs, create routes, read routes, update routes, delete routes, database code, authentication, or a frontend today.

---

## Technical Deliverables

☐ Keep the existing `GET /health` route unchanged.

☐ Change `GET /notes` from a placeholder error response to a successful empty collection response.

☐ Make `GET /notes` return HTTP status `200` and JSON exactly equal to `{"notes": []}`.

---

## Definition of Done

After synchronizing dependencies with `uv sync`, `uv run flask --app src.harbor routes` shows both `/health` and `/notes`. `curl -i http://127.0.0.1:5000/notes` returns HTTP status `200`, a JSON response, and a body that parses to exactly `{"notes": []}`. Harbor still has no note storage, no sample notes, no note schema, no create route, no read-one route, no update route, no delete route, no database code, no authentication, and no frontend.

---

## Tomorrow Depends On

Tomorrow depends on Harbor returning an empty notes collection before it accepts a new note.

---

## My Reflection

Where are you tempted to call something unfinished when faithfulness would make even the empty case dependable?

Myself, in my current unemployment I am empty right now. Yet my career is not "unfinished" it is simply dependably empty in this season.