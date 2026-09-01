<!--
name: 'Skill: Code Review (Phase 3 — sweep for gaps)'
description: >-
  Shared Phase 3 of the code-review skill — a fresh finder re-reads the diff for
  defects not already listed
ccVersion: 2.1.214
variables:
  - SKILL_CODE_REVIEW_PHASE_3_SWEEP_2_VAR_0
-->

## Phase 3 — Sweep for gaps

Take one more pass yourself (same context, no subagent) as a fresh reviewer
who has the deduplicated list. Re-read the diff and enclosing functions
looking only for defects not already listed: ${SKILL_CODE_REVIEW_PHASE_3_SWEEP_2_VAR_0}
