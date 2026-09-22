<!--
name: 'Skill: Code Review (Phase 3 — sweep for gaps)'
description: >-
  Shared Phase 3 of the code-review skill — a fresh finder re-reads the diff for
  defects not already listed
ccVersion: 2.1.214
variables:
  - SWEEP_MISS_CATEGORIES
-->
## Phase 3 — Sweep for gaps

Run one more finder as a fresh reviewer who has the verified list. Re-read the
diff and enclosing functions looking ONLY for defects not already listed. Do not
re-derive or re-confirm anything already there — the job is gaps. Focus
on what the first pass tends to miss: ${SWEEP_MISS_CATEGORIES}

Surface up to 8 additional candidates, each naming a defect not already on the
list. If nothing new, return an empty sweep — do not pad.
