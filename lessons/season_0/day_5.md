# Season 0 • Day 5

## Today's Scene

Ruth reaches the clinic before the first appointment reminder goes out. The waiting room is still dark, the coffee machine is warming, and the phone on her desk already has two blinking messages. She runs the program to see the next appointment action, expecting the familiar requirement sentence that has helped her close the loop for one family at a time.

Instead, the screen fills with a traceback. File paths. Line numbers. A `ValueError`. Words that are true to an engineer but useless to Ruth in the moment. The program has done the honest thing by refusing incomplete data, but it has not yet done the serving thing by explaining the failure in a way she can act on.

One engineer says the traceback is enough because the bug is obvious. Another starts proposing a logging system, error codes, and a help page. You look at Ruth's desk, the waiting calls, and the small broken data file. Service chooses the narrow repair: one clear error line that names the missing field and tells the next action. Not a lecture. Not a dump of internals. Just enough truth to help the person in front of the software take the next faithful step.

---

## Scripture

Mark 10:45

---

## Formation

Service

---

## Engineering Principle

A useful error message names the problem and the next action.

---

## Technical Source

Python 3 `unittest` documentation

---

## Today's Build

Update the saved-data validation in `src/serve_one_person.py` so the first invalid field raises `ValueError` with this exact message form: `Saved requirement is incomplete: <field> is required. Add a non-empty <field> value to the saved requirement file.` Keep validating `person`, `task`, and `success` in that order. Update the invalid-data test so injecting `tests/data/incomplete_ruth_requirement.json` into `main` proves the exact error message is `Saved requirement is incomplete: success is required. Add a non-empty success value to the saved requirement file.` Do not change command-line arguments, the default data file, or the valid requirement sentence today.

---

## Technical Deliverables

☐ Update the validation error message so it names the invalid field and the next action.

☐ Update the invalid-data test to assert the exact `ValueError` message for `tests/data/incomplete_ruth_requirement.json`.

☐ Keep the valid-data test proving the default requirement sentence still prints exactly.

---

## Definition of Done

Running `python src/serve_one_person.py` prints exactly `Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work.` Running `python -m unittest tests/test_serve_one_person.py` completes with `OK`. The test suite fails if injecting `tests/data/incomplete_ruth_requirement.json` into `main` does not raise `ValueError` with exactly `Saved requirement is incomplete: success is required. Add a non-empty success value to the saved requirement file.`

---

## Tomorrow Depends On

Tomorrow depends on the program naming invalid saved data with one actionable validation message.

---

## My Reflection

Where have you told someone what failed without telling them the next faithful action they could take?

When I'd run a loader as part of an ETL process that relied on a configuration file to exist in S3, the loader would fail with an S3 error but not tell the user the next actionable step: that they needed to load the configuration file and ensure it had the correct values set for each field relevant to the loader and their situation.