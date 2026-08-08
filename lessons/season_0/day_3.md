# Season 0 • Day 3

## Today's Scene

Ruth runs the command again just before closing. The clinic lobby has gone still, but her desk is not still: one hand on the phone, one eye on the appointment list, one more family waiting for the right call. The program works, but it asks her to type the same person, task, and success condition every time she needs the sentence.

The team notices the friction and immediately reaches for a larger answer. Someone sketches user accounts. Someone suggests a database. Someone says this is really a profile-management problem. The ideas are not foolish, but they are too heavy for the need in front of them.

You look at Ruth's three repeated pieces of information and choose the smaller stewardship: put them in one plain data file. The program should remember what Ruth should not have to carry. Not forever. Not for every possible clinic. Just for this one next step.

---

## Scripture

1 Peter 4:10

---

## Formation

Stewardship

---

## Engineering Principle

A tiny data file keeps repeated user information in one durable place.

---

## Technical Source

Python 3 `json` documentation

---

## Today's Build

Create `data/ruth_requirement.json` containing Ruth's saved `person`, `task`, and `success` values. Update `src/serve_one_person.py` so running `python src/serve_one_person.py` with no arguments reads that file and prints the same requirement sentence Ruth already depends on.

---

## Technical Deliverables

☐ Create `data/ruth_requirement.json` with exactly these keys: `person`, `task`, and `success`.

☐ Store these exact values in the file: `Ruth`, `see the next appointment action`, and `she can call the right family before leaving work`.

☐ Update the existing single test in `tests/test_serve_one_person.py` so it runs `python src/serve_one_person.py` with no arguments and verifies the exact requirement sentence.

---

## Definition of Done

Running `python src/serve_one_person.py` prints exactly `Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work.` Running `python -m unittest tests/test_serve_one_person.py` completes with `OK`. Searching `src/serve_one_person.py` for `Ruth`, `see the next appointment action`, or `call the right family` returns no matches.

---

## Tomorrow Depends On

Tomorrow depends on having Ruth's repeated requirement stored in one tiny data file that the program reads by default.

---

## My Reflection

What burden are you asking someone to carry again because the software has not yet learned how to remember it once?

They often carry the burden of their own limitations and now the software's limitations as well. Humans can only remember so much information so when they are forced to now carry the burden of remembering information your software uses regularly while still having to carry the burden of getting their task done, you have done them a disservice.