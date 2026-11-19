<!--
name: 'Agent Prompt: /code-review part 2 low effort mode'
description: >-
  Low-effort /code-review prompt that reads the diff once and returns up to four
  hunk-visible runtime correctness findings
ccVersion: 2.1.328
variables:
  - SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_0
  - SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_1
  - SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_2
  - SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_3
  - SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_4
  - SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_5
  - SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_6
-->
\`low effort → 1 diff pass${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_0?" (bugs)":""} → no verify → ${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_1(SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_2)}\`

## Turn 1 — read

One tool call: read the unified diff (\`git diff @{upstream}...HEAD; git diff HEAD\`
to cover both committed and uncommitted changes, or \`git diff main...HEAD\` /
the target passed as an argument). Skip test/fixture
hunks (\`test/\`, \`spec/\`, \`__tests__/\`, \`*_test.*\`, \`*.test.*\`,
\`fixtures/\`, \`testdata/\`) — test-file changes are not reviewed at this level.
No subagents, no full-file reads.

## Turn 2 — findings

Flag runtime-correctness bugs visible from the hunk alone: inverted/wrong
condition, off-by-one, null/undefined deref where adjacent lines show the value
can be absent, removed guard, falsy-zero check, missing \`await\`,
wrong-variable copy-paste, error swallowed in a catch that should propagate.${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_0?"":`
Also flag — still from the hunk alone — new code that duplicates an existing
helper visible in the diff context, and dead code the diff leaves behind.`}

Do **not** flag style, naming, perf, missing tests, or anything outside the
hunk.

${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_3?`Report ${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_4(SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_2)}, most-severe first, in one
${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_5} call with \`{level, findings}\` — each entry has
\`file\`, \`line\`, \`summary\`, \`short_summary\` (≤60 characters), ${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_0?"`severity`, ":""}and
\`failure_scenario\`.${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_0?` Every entry's \`severity\` is one of ${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_6} End each \`summary\` with "Fix:" and the change to make, or what to check if you are not sure.`:""} If nothing qualifies, call it with an empty findings
array. Do not also print the findings as text.
`:`Output ${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_4(SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_2)}, most-severe first, one line each:
\`path/to/file.ext:123 — ${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_0?"important|pre_existing|nit — ":""}what's wrong and the concrete failure${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_0?". Fix: the change to make, or what to check if you are not sure":""}\`.${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_0?` Every line carries one of those three words: ${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_6}`:""} If nothing
qualifies, output exactly \`(none)\`. Do not call the
${SKILL_CODE_REVIEW_EFFORT_LOW_2_VAR_5} tool even if it is available.
`}
