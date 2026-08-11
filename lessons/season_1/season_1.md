# Season 1

## Theme

Building Something That Works

## Season Question

How do I faithfully turn a person's need into working software?

## Duration

14 Days, Day 0 through Day 13

## Final Artifact

Harbor v1: a small complete HTTP API for creating, retrieving, updating, listing, and deleting notes.

## Formation Outcome

The reader becomes a careful builder who listens before assuming, chooses deliberately, verifies work, and remembers the person being served.

## Engineering Outcome

The reader understands how a human need moves through requirement, HTTP request, application logic, persistence, response, and verification.

## Technical Stack

Python, Flask, SQLite with Python's built-in `sqlite3`, and pytest.

## Constraints

No Django, ORM, Redis, queues, microservices, Docker, cloud infrastructure, authentication, async frameworks, or frontend frameworks. Introduce structure only when Harbor feels the pain it solves, and prefer Flask-native patterns when structure becomes necessary. Each day stays small enough for one sitting and follows RULE.md.

## Lesson Progress

| Day | Formation | Focus |
| --- | --- | --- |
| Day 0 | Service | Define Harbor's user and need |
| Day 1 | Humility | HTTP request and response |
| Day 2 | Clarity | Resources and URLs |
| Day 3 | Faithfulness | GET a collection of notes |
| Day 4 | Responsibility | POST a new note |
| Day 5 | Stewardship | Persist notes with SQLite |
| Day 6 | Wisdom | Model note data deliberately |
| Day 7 | Integrity | Validate bad input |
| Day 8 | Care | Retrieve one note |
| Day 9 | Responsibility | Update one note |
| Day 10 | Stewardship | Delete one note safely |
| Day 11 | Humility | Handle errors intentionally |
| Day 12 | Integrity | Test expected behavior with pytest |
| Day 13 | Faithfulness | Prove Harbor works end-to-end and review the season |

## Day 13 Done Condition

Harbor v1 is done when pytest passes and one end-to-end verification proves a note can be created, listed, retrieved, updated, deleted, and confirmed absent through the HTTP API while using SQLite persistence.
