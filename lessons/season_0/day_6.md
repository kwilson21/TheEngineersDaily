# Season 0 • Day 6

## Today's Scene

The handoff meeting is small: Ruth, one engineer, and a laptop balanced on the corner of her desk before the clinic opens. The command has learned her repeated requirement. It can read the saved JSON file, protect the exact sentence with tests, and refuse incomplete data with an actionable message. It is almost ready to leave the safety of the repository and become a tool in Ruth's morning.

But Ruth will not meet the program inside a test runner. She will meet it at the command line, between a blinking cursor and the next family she needs to call. A teammate suggests adding a setup wizard. Another says the traceback is fine because the validation message is somewhere inside it. Both answers make the doorway heavier than it needs to be.

Wisdom chooses the narrow polish. When the saved requirement is whole, the command should say the requirement and nothing else. When the saved requirement is broken, the command should give one clear error line, hide the internal noise, and exit in a way the system can understand. The final gift is not decoration. It is gentle clarity at the boundary where Ruth actually touches the work.

---

## Scripture

James 3:17

---

## Formation

Wisdom

---

## Engineering Principle

A polished command-line program keeps success and expected failure understandable at the command boundary.

---

## Technical Source

Python 3 `sys` documentation

---

## Today's Build

Add one command-boundary wrapper to `src/serve_one_person.py` without changing the saved requirement file, the requirement sentence, or the command-line arguments. The wrapper must return an integer status code so tests can assert the boundary without starting a subprocess. On success, it must print the requirement sentence to standard output, print nothing to standard error, and return `0`. When validation raises `ValueError`, it must print exactly the error message to standard error, print nothing to standard output, and return `1`. The `if __name__ == "__main__"` block must pass that return value to `sys.exit`.

---

## Technical Deliverables

☐ Add a `run_cli(data_file_path=...)` boundary function that calls `main`, prints the successful result to standard output, catches `ValueError`, prints its message to standard error, and returns `0` or `1`.

☐ Update the `if __name__ == "__main__"` block so the process exits with the code returned by `run_cli()`.

☐ Update automated tests to call `run_cli(...)` directly, capture standard output and standard error, and verify both the success boundary and the expected validation failure boundary using `tests/data/incomplete_ruth_requirement.json`.

---

## Definition of Done

Running `python src/serve_one_person.py` exits with code `0`, writes exactly `Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work.` to standard output, and writes nothing to standard error. Running `python -m unittest tests/test_serve_one_person.py` completes with `OK`. The tests fail if `run_cli()` returns anything other than `0`, writes the success sentence anywhere except standard output, or writes anything to standard error. The tests also fail if `run_cli("tests/data/incomplete_ruth_requirement.json")` returns anything other than `1`, writes anything to standard output, or writes anything to standard error other than exactly `Saved requirement is incomplete: success is required. Add a non-empty success value to the saved requirement file.`

---

## Tomorrow Depends On

Tomorrow depends on having one polished command boundary that Ruth can trust in success and expected failure.

---

## My Reflection

Where do you need wisdom to make the next action plain instead of making the system sound impressive?

For my next app idea, I can utilize wisdom to resist a fancy front-end and back-end system design and just do the bare minimum to get a reliable working idea that is simple enough for me to use everyday.