<!--
name: 'Skill: Code Review (xhigh effort, inline single-pass)'
description: >-
  Effort-tier prompt for the inline xhigh code review — 10 angles run in-context
  with no subagents, dedup only (no verify), sweep, up to 15 findings. Reshaped
  in 2.1.214; the fan-out variant now lives in skill-code-review-effort-max-3.
ccVersion: 2.1.328
variables:
  - FORMAT_FINDINGS_LIMIT_LABEL_FN
  - MAX_FINDINGS
  - PHASE_0_GATHER_DIFF
  - CORRECTNESS_ANGLES
  - EXTRA_CORRECTNESS_ANGLES
  - ANGLE_REUSE
  - ANGLE_SIMPLIFICATION
  - ANGLE_EFFICIENCY
  - ANGLE_ALTITUDE
  - ANGLE_CONVENTIONS
  - CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE
  - INLINE_GAP_SWEEP_PHASE
  - FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN
  - OUTPUT_FORMAT_FN
-->
\`xhigh effort → 10 inline angles → dedup (no verify) → sweep → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}\`

You are reviewing for **recall** at extra-high effort: catch every real bug. At
this level, catching real bugs matters more than avoiding false positives — a
missed bug ships. Err on the side of surfacing.

${PHASE_0_GATHER_DIFF}
## Phase 1 — Find candidates (5 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 8 each)

Run **10 independent finder angles** in sequence yourself, in this context — spawn no subagents for them. Each
surfaces **up to 8 candidate findings**. Don't let one angle's conclusions
suppress another's — if two angles flag the same line for different reasons,
record both.

${CORRECTNESS_ANGLES}
${EXTRA_CORRECTNESS_ANGLES}
${ANGLE_REUSE}
${ANGLE_SIMPLIFICATION}
${ANGLE_EFFICIENCY}
${ANGLE_ALTITUDE}
${ANGLE_CONVENTIONS}
${CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE}
## Phase 2 — Dedup only (no verify)

Pool all candidates. Dedup near-duplicates only (same defect, same location, same reason → keep one). Skip the verifiers and leave each candidate's judgment as it stands. Sort by severity. Keep the ones you're uncertain about.

## Phase 3 — Sweep for gaps

${INLINE_GAP_SWEEP_PHASE}
${FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN(OUTPUT_FORMAT_FN,15)(MAX_FINDINGS)}
