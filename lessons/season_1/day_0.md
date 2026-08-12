# Season 1 • Day 0

## Today's Scene

The last command-line lesson is closed, and Ruth's small tool is steady enough to hand back to the work it serves. The repository is quiet for a moment. Then the next request arrives with a bigger name: Harbor, a small HTTP API for notes.

The room starts filling with guesses before the problem has a face. One engineer opens a blank Flask file. Another sketches tables. Someone says notes need tags, search, accounts, timestamps, and probably a frontend someday. The whiteboard gets full, but the person served by the work is still missing.

Then Mara joins the call from a dim operations room, her headset on, an incident timeline open beside a terminal. She is not asking for a grand notes platform. During handoff, she needs one dependable place where short notes can be created, found, corrected, and removed through an API her tools can call. Service stops the rush toward impressive machinery and writes the first Harbor artifact as a plain promise: who this serves, what need it meets, and what useful will mean.

---

## Scripture

Mark 10:45

---

## Formation

Service

---

## Engineering Principle

Software should begin with a named person, a concrete need, and a clear definition of useful.

---

## Technical Source

RFC 8259 - The JavaScript Object Notation (JSON) Data Interchange Format

---

## Today's Build

Create one requirement file at `data/harbor_need.json`. Do not create or edit Harbor application code in `src/` today. The file must contain exactly this JSON:

```json
{
    "user": "Mara, an on-call engineer who writes incident handoff notes between alerts",
    "need": "store and retrieve short incident notes through a small HTTP API",
    "success": "she can create, list, read, update, and delete notes without losing the latest note text"
}
```

---

## Technical Deliverables

☐ Create `data/harbor_need.json`.

☐ Store exactly these values: `user` is `Mara, an on-call engineer who writes incident handoff notes between alerts`, `need` is `store and retrieve short incident notes through a small HTTP API`, and `success` is `she can create, list, read, update, and delete notes without losing the latest note text`.

☐ Leave `src/` unchanged today.

---

## Definition of Done

`data/harbor_need.json` exists, its contents match the JSON in Today's Build, and `python -m json.tool data/harbor_need.json` succeeds. No Harbor application code exists in `src/` yet.

---

## Tomorrow Depends On

Tomorrow depends on Harbor having one saved user, need, and success condition before any HTTP route exists.

---

## My Reflection

Where are you tempted to start building before you have named the person your software must serve?

I immediately start thinking about the database design, how the notes will be stored and the API design such as what HTTP methods will be used.