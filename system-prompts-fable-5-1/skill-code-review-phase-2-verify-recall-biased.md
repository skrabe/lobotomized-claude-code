<!--
name: 'Skill: Code Review (Phase 2 — verify, recall-biased)'
description: >-
  Phase 2 of the code-review skill for recall tiers — one verifier per
  candidate, recall-biased keep rule
ccVersion: 2.1.160
variables:
  - AGENT_TOOL_NAME
-->
## Phase 2 — Verify (1-vote, recall-biased)

Dedup near-duplicates (same defect, same location, same reason → keep one). For
each remaining candidate, run one verifier via the ${AGENT_TOOL_NAME} tool:
give it the diff, the relevant file(s), and the candidate; it returns exactly
one of **CONFIRMED / PLAUSIBLE / REFUTED**.

${RECALL_BIASED_RUBRIC}

Keep CONFIRMED and PLAUSIBLE. Drop REFUTED.
