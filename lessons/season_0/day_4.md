# Season 0 • Day 4

## Today's Scene

The JSON file sits quietly in the repository, small enough to look harmless. Ruth has gone home for the evening. The clinic lights are low, the hallway floor is being mopped, and tomorrow's appointment list is already waiting for the first phone call.

While cleaning up a branch, an engineer opens `data/ruth_requirement.json` to check the saved values. The `person` is still Ruth. The `task` is still clear. But the `success` line has been accidentally removed during a copy-and-paste. The file still looks like data. The program can still open it. The danger is that the software may speak with confidence when the truth it needs is incomplete.

Integrity begins before the output line appears. A faithful program must not pretend that partial data is a complete requirement. It must inspect what it has been given, refuse what is incomplete, and only speak Ruth's requirement when the saved data is whole.

---

## Scripture

Proverbs 11:3

---

## Formation

Integrity

---

## Engineering Principle

Validate saved data before trusting it.

---

## Technical Source

Python 3 function definitions documentation

---

## Today's Build

Update `src/serve_one_person.py` so Ruth's saved requirement is validated before the requirement sentence is built. Keep normal program behavior pointed at `data/ruth_requirement.json`. For the invalid-data test, create exactly one fixture file at `tests/data/incomplete_ruth_requirement.json` with exactly this content:

```json
{
    "person": "Ruth",
    "task": "see the next appointment action"
}
```

Use dependency injection for the file path: update `main` so it accepts an optional `data_file_path` argument that defaults to `data/ruth_requirement.json`. The normal command still uses the real saved requirement, while the invalid-data test injects `tests/data/incomplete_ruth_requirement.json` by passing that path into `main`. The test must not edit, overwrite, or temporarily corrupt `data/ruth_requirement.json`. The saved data is valid only when `person`, `task`, and `success` all exist, each value is a string, and each value contains at least one non-whitespace character. If the first invalid field is found, raise `ValueError` with exactly this message: `Saved requirement is incomplete: <field> is required.`

---

## Technical Deliverables

☐ Use dependency injection by updating `main` to accept one optional `data_file_path` argument that defaults to `data/ruth_requirement.json`.

☐ Add a validation step before formatting the requirement sentence, checking `person`, `task`, and `success` in that order.

☐ Create `tests/data/incomplete_ruth_requirement.json` with the exact JSON from Today's Build, then add one automated test that injects that path into `main` and proves it raises `ValueError` with exactly `Saved requirement is incomplete: success is required.`

---

## Definition of Done

Running `python src/serve_one_person.py` with the unchanged `data/ruth_requirement.json` prints exactly `Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work.` Running `python -m unittest tests/test_serve_one_person.py` completes with `OK`. The invalid-data test injects `tests/data/incomplete_ruth_requirement.json` into `main`, and the test suite fails if that incomplete fixture can produce a requirement sentence.

---

## Tomorrow Depends On

Tomorrow depends on the program refusing to build a requirement sentence from incomplete saved data.

---

## My Reflection

Where are you tempted to let software say something is complete before you have checked whether it is true?

Typically when working on software that I have built from the ground up fast. I let my own experience with the software be the assertion that it's complete. This works well when you want to move fast, but it destroys the program's integrity in the long run, will I be able to remember all of these things a year or more from now?
