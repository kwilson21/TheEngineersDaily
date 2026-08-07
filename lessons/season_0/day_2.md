# Season 0 • Day 2

## Today's Scene

Ruth runs yesterday's command near the end of a long clinic day. The lobby lights are dimmed, the printer is finally quiet, and one family still needs a call before she can leave. The program prints the requirement sentence she has been using to keep the next action clear.

Across town, the team is cleaning up the code. Someone changes the wording because it sounds smoother. Someone else removes the final period because it looks unnecessary. The program still opens. It still prints words. No alarm sounds. But Ruth's small workflow now depends on a promise nobody is checking.

A faithful engineer does not wait for a person to rediscover a broken promise by hand. Before adding anything new, you place one small automated test beside the program. It watches the sentence Ruth depends on and checks the same promise every time the command runs.

---

## Scripture

Luke 16:10

---

## Formation

Faithfulness

---

## Engineering Principle

A small automated test protects the behavior the user depends on.

---

## Technical Source

Python 3 `subprocess` documentation

---

## Today's Build

Create `tests/test_serve_one_person.py` with exactly one automated test. Use Python's standard-library `unittest` and `subprocess.run` to run `python src/serve_one_person.py --person Ruth --task "see the next appointment action" --success "she can call the right family before leaving work"` the same way Ruth would run it. Capture the output and verify the command exits successfully and prints one output line exactly equal to `Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work.`

---

## Technical Deliverables

☐ Create `tests/test_serve_one_person.py`.

☐ Use Python's standard-library `unittest` runner with exactly one test method.

☐ In that test, execute the Day 1 command with `subprocess.run`, `capture_output=True`, and `text=True`, then assert exit code `0` and that `stdout.strip()` equals the exact sentence from Today's Build.

---

## Definition of Done

Running `python -m unittest tests/test_serve_one_person.py` completes with `OK`. The test fails if the program's only output line is not exactly `Requirement: Ruth needs to see the next appointment action so that she can call the right family before leaving work.`

---

## Tomorrow Depends On

Tomorrow depends on having one automated test that proves Ruth's exact requirement sentence still holds.

---

## My Reflection

What small promise in your work needs a faithful check before it quietly breaks for someone else?

My promise of completing a ticket needs a faithful check. Sometimes I do not do the due diligence I should to ensure that a ticket actually has the details needed to guarantee that valid promise can be made and validated via my work. Therefore, it's all the more important that I ensure that a ticket has requirements that I can meet so that I can build faithful checks in my promised remediation to the ticket. I never want my unchecked promises to cause pain for someone else and performing a faithful check would help.