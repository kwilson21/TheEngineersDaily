# Season 0 • Day 0

## Today's Scene

The first ticket looks small: add a text box and a button to an internal tool used by a clinic scheduler named Ruth. The team chat is already alive with bigger ideas. One engineer wants a new framework. Another wants a smarter data model. A third suggests postponing the ticket until the whole scheduling system can be redesigned.

You open the support notes and find the real weight of the request. Ruth is calling families after hours because one missing note hides the next step in each appointment. The work is not glamorous. It will not impress anyone in a demo. But if the tool clearly shows the next action, Ruth can finish on time, families get called sooner, and the software becomes a quiet act of service instead of a polished distraction.

Before writing code, you write one sentence on the whiteboard: "This program serves Ruth by helping her see the next appointment action."

---

## Scripture

Colossians 3:23

Psalm 127:1

---

## Formation

Calling

---

## Engineering Principle

Software exists to serve people.

---

## Technical Source

Python 3 `argparse` documentation

---

## Today's Build

Create a single command-line program named `src/serve_one_person.py` that accepts `--person` and `--task`, rejects empty values, and prints one sentence naming who the program serves and what it helps that person do.

---

## Technical Deliverables

☐ Create `src/serve_one_person.py`.

☐ Parse required `--person` and `--task` arguments and reject empty values.

☐ Print exactly one service sentence in the form: `This software serves <person> by helping them <task>.`

---

## Definition of Done

Running `python src/serve_one_person.py --person Ruth --task "see the next appointment action"` prints exactly `This software serves Ruth by helping them see the next appointment action.` Running the same command with an empty `--person` or empty `--task` exits with an error.

---

## Tomorrow Depends On

Tomorrow depends on having a program whose purpose is stated in terms of one person served and one task helped.

---

## My Reflection

Where are you tempted to make the work impressive before you have made it useful to the person it serves?

I often want to learn something new or use a new technique or new framework to bolster my tech skills before I have even considered making the software more useful to the person it serves. I also sometimes want the work to look good so that it is enticing to the user first.
