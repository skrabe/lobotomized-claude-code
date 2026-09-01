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
diff and enclosing functions looking only for defects not already listed. Don't
re-derive anything already there — the job is gaps. Focus on what the first pass
tends to miss: moved/extracted code that dropped a guard or anchor; second-tier
footguns (dataclass default evaluated once, \`hash()\` non-determinism,
lock-scope shrink, predicate methods with side effects); setup/teardown
asymmetry in tests; config defaults flipped.

Surface up to 8 additional candidates, each naming a defect not already on the
list. If nothing new, return an empty sweep — do not pad.
