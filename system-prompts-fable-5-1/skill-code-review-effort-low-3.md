<!--
name: 'Skill: Code Review (low effort)'
description: >-
  Effort-tier prompt for low code review — single diff pass, no verify, up to 4
  findings
ccVersion: 2.1.218
variables:
  - SKILL_CODE_REVIEW_EFFORT_LOW_3_VAR_0
  - SKILL_CODE_REVIEW_EFFORT_LOW_3_VAR_1
-->
\`low effort → 1 diff pass → no verify → ≤8 findings\`

## Turn 1 — read

One tool call: read the unified diff (\`git diff @{upstream}...HEAD; git diff HEAD\`
to cover both committed and uncommitted changes, or \`git diff main...HEAD\` /
the target passed as an argument). No subagents, no full-file reads.

## Turn 2 — findings

Flag runtime-correctness bugs visible from the hunk alone: inverted/wrong
condition, off-by-one, null/undefined deref where adjacent lines show the value
can be absent, removed guard, falsy-zero check, missing \`await\`,
wrong-variable copy-paste, error swallowed in a catch that should propagate.
Also flag — still from the hunk alone — new code that duplicates an existing
helper visible in the diff context, and dead code the diff leaves behind.

Do **not** flag style, naming, perf, missing tests, or anything outside the
hunk.

${SKILL_CODE_REVIEW_EFFORT_LOW_3_VAR_0?`Report at most **8 findings**, most-severe first, in one
${SKILL_CODE_REVIEW_EFFORT_LOW_3_VAR_1} call with \`{level, findings}\` — each entry has
\`file\`, \`line\`, \`summary\`, \`short_summary\` (≤60 characters), and
\`failure_scenario\`.
Target at least min(files_changed, 4) findings — if you see fewer, widen to other hunks in the same diff before stopping. If fewer than 4 genuine findings exist, report what you have. Do not also print the findings as text.
`:`Output at most **8 findings**, most-severe first, one line each:
\`path/to/file.ext:123 — what's wrong and the concrete failure\`.
Target at least min(files_changed, 4) findings — if you see fewer, widen to other hunks in the same diff before stopping. If fewer than 4 genuine findings exist, emit what you have.
`}
