<!--
name: 'Skill: Code Review (max / xhigh effort)'
description: >-
  Effort-tier prompt for max and xhigh code review — 5 angles, up to 8
  candidates, recall-biased, up to 15 findings
ccVersion: 2.1.328
variables:
  - FORMAT_FINDINGS_LIMIT_LABEL_FN
  - MAX_FINDINGS
  - PHASE_0_GATHER_DIFF
  - CORRECTNESS_ANGLES
  - EXTRA_CORRECTNESS_ANGLES
  - ANGLE_CONVENTIONS
  - CONVENTIONS_CANDIDATES_NOTE_FN
  - INLINE_GAP_SWEEP_PHASE
  - FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN
  - OUTPUT_FORMAT_FN
  - FINDING_SEVERITY_OUTPUT_OPTIONS
-->
\`xhigh effort → 6 inline angles (bugs + conventions) → dedup (no verify) → sweep → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}\`

You are reviewing for **recall** at extra-high effort: catch every real bug. Err on the side of surfacing.

${PHASE_0_GATHER_DIFF}
## Phase 1 — Find candidates (5 correctness angles + 1 conventions angle, up to 8 each)

Run **6 independent finder angles** in sequence yourself, in THIS context — do NOT spawn subagents for them. Each
surfaces **up to 8 candidate findings**. Do NOT let one angle's conclusions
suppress another's — if two angles flag the same line for different reasons,
record both.

${CORRECTNESS_ANGLES}
${EXTRA_CORRECTNESS_ANGLES}
${ANGLE_CONVENTIONS}
${CONVENTIONS_CANDIDATES_NOTE_FN("the output's")}
Pass every candidate with a nameable failure scenario through — finders that
silently drop half-believed candidates are the dominant cause of misses.

## Phase 2 — Dedup only (no verify)

Pool all candidates. Dedup near-duplicates only (same defect, same location, same reason → keep one). Do NOT run verifiers; do NOT re-judge. Sort by severity. Do NOT drop on uncertainty.

## Phase 3 — Sweep for gaps

${INLINE_GAP_SWEEP_PHASE}
Then give each finding, the sweep's too, its \`severity\`, as Output defines it.

${FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN(OUTPUT_FORMAT_FN,15)(MAX_FINDINGS,FINDING_SEVERITY_OUTPUT_OPTIONS)}
