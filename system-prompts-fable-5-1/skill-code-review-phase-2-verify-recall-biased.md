<!--
name: 'Skill: Code Review (Phase 2 — verify, recall-biased)'
description: >-
  Phase 2 of the code-review skill for recall tiers — one verifier per
  candidate, recall-biased keep rule
ccVersion: 2.1.160
variables:
  - AGENT_TOOL_NAME
  - RECALL_BIASED_RUBRIC
-->
## Phase 2 — Verify (1-vote, recall-biased)

Dedup near-duplicates (same defect, same location, same reason → keep one). For
each remaining candidate, run one verifier via the ${AGENT_TOOL_NAME} tool:
give it the diff, the relevant file(s), and the candidate; it returns exactly
one of **CONFIRMED / PLAUSIBLE / REFUTED**.

**PLAUSIBLE by default** — do not refute a candidate for being "speculative" or
"depends on runtime state" when the state is realistic: concurrency races,
nil/undefined on a rare-but-reachable path (error handler, cold cache, missing
optional field), falsy-zero treated as missing, off-by-one on a boundary the
code does not exclude, retry storms / partial failures, regex/allowlist that
lost an anchor.

**REFUTED** only when constructible from the code: factually wrong (quote the
actual line); provably impossible (type/constant/invariant — show it); already
handled in this diff (cite the guard); or pure style with no observable effect.

Keep CONFIRMED and PLAUSIBLE. Drop REFUTED.
