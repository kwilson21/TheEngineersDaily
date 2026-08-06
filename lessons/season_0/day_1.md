# Season 0 • Day 1

## Today's Scene

Ruth joins the call from a small office beside the clinic lobby. Behind her, the printer clicks, the phone rings twice, and a stack of appointment folders leans against her keyboard. Yesterday's program can say who it serves and what task it helps, but the team is still guessing at what "help" really means.

One engineer starts listing features: color tags, sorting, a dashboard, maybe a reminder system later. Ruth waits politely. Then someone asks the slower question: "What would make this finished enough for you to trust it today?"

Ruth looks down at the folders and says, "I need to see the next appointment action so I can call the right family before I leave work. If I still have to open three screens to check that, I will keep using sticky notes."

The room gets quiet. The better requirement is not bigger. It is humbler. It stops performing certainty and starts receiving the truth from the person being served.

---

## Scripture

James 1:19

Proverbs 18:13

---

## Formation

Humility

---

## Engineering Principle

A useful requirement names the user, the need, and the success condition.

---

## Technical Source

Python 3 `argparse` documentation

---

## Today's Build

Extend `src/serve_one_person.py` so it accepts a required `--success` argument in addition to yesterday's `--person` and `--task`, rejects blank values for all three arguments, and prints one requirement sentence in the form: `Requirement: <person> needs to <task> so that <success>.`

---

## Technical Deliverables

☐ Add a required `--success` argument.

☐ Reject blank `--person`, `--task`, and `--success` values.

☐ Print exactly one requirement sentence in the form: `Requirement: <person> needs to <task> so that <success>.`

---

## Definition of Done

Running `python src/serve_one_person.py --person Ruth --task "see the next appointment action" --success "she can call the right family before leaving work"` prints exactly `Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work.` Running the same command with an empty `--person`, empty `--task`, or empty `--success` exits with an error.

---

## Tomorrow Depends On

Tomorrow depends on having a requirement sentence with a named person, a task, and an observable success condition.

---

## My Reflection

Whose voice do you need to hear before you decide what the software should do?

I need to hear a user or customer's voice. Without that, I cannot be so sure about who I am serving.