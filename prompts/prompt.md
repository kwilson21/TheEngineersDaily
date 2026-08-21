Read RULE.md, LESSON_TEMPLATE.md, and CURRENT_STATE.md.

Generate today's lesson by following the lesson template exactly.

Requirements:

- Preserve curriculum continuity.
- Paint a vivid engineering parable.
- Teach exactly one engineering principle.
- Cultivate exactly one biblical virtue.
- Provide one objective technical implementation for the learner to complete.
- Do not write, edit, or solve the lesson application code yourself.
- Write one reflection question that naturally emerges from the story.
- Update CURRENT_STATE.md for tomorrow.
- Generate exactly one suggested git commit subject for today's completed lesson using this format: `Add Season <season number> Day <day number> <concise lowercase lesson focus> lesson`. Derive the focus from today's engineering work, use no conventional-commit prefix or ending punctuation, and do not offer alternatives. Example: `Add Season 1 Day 9 note update lesson`.

Reduce ambiguity whenever possible.

Protect simplicity above all else.

Directory conventions:

- Save lessons in `lessons/season_X/day_X.md`.
- Save season definitions in `lessons/season_X/season_X.md`.
- Lesson application code belongs in `src/` when the learner writes it.
- Keep `RULE.md`, `LESSON_TEMPLATE.md`, and `CURRENT_STATE.md` at the repository root.
