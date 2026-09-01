<!--
name: 'Workflow: /simplify cleanup agents'
description: 'Workflow: /simplify cleanup agents'
ccVersion: 2.1.156
variables:
  - PROMPT_VAR_0
  - PROMPT_VAR_1
  - PROMPT_VAR_2
  - PROMPT_VAR_3
  - PROMPT_VAR_4
  - PROMPT_VAR_5
-->
\`/simplify → 4 cleanup agents in parallel → apply the fixes\`

Review it for reuse, simplification, efficiency, and altitude issues, then fix what you
find. Do not look for correctness bugs — that is what \`/code-review\` is for.

${PROMPT_VAR_0}
## Phase 1 — Review (4 cleanup agents in parallel)

Launch **4 independent review agents** via the ${PROMPT_VAR_1} tool, all in a
single message so they run concurrently. Pass each agent the diff and one of
the four angles below. Each returns its findings with \`file\`, \`line\`, a
one-line \`summary\`, and the concrete cost (what is duplicated, wasted, or
harder to maintain).

### Reuse

${PROMPT_VAR_2}
${PROMPT_VAR_3}
${PROMPT_VAR_4}
${PROMPT_VAR_5}
## Phase 2 — Apply the fixes

Wait for all four agents to complete, dedup findings that point at the same
line or mechanism, and fix each remaining one directly. Skip any finding whose
fix would change intended behavior, require changes well outside the reviewed
diff, or that you judge to be a false positive — note the skip rather than
arguing with it. Finish with a brief summary of what was fixed and what was
skipped (or confirm the code was already clean).
