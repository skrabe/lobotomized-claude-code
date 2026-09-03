<!--
name: 'Skill: Code Review (Phase 2 — verify, 3-state)'
description: >-
  Phase 2 of the code-review skill for precision tiers — one verifier per
  candidate, 3-state CONFIRMED/PLAUSIBLE/REFUTED vote
ccVersion: 2.1.160
variables:
  - AGENT_TOOL_NAME
  - VERIFY_VOTE_DEFINITIONS
-->
## Phase 2 — Verify (1-vote, 3-state)

Dedup candidates that point at the same line/mechanism, keeping the one with
the most concrete failure scenario. For each remaining candidate, run one
verifier via the ${AGENT_TOOL_NAME} tool: give it the diff, the relevant
file(s), and the candidate, and have it return exactly one of:

${VERIFY_VOTE_DEFINITIONS}

Keep candidates voted CONFIRMED or PLAUSIBLE.
