<!--
name: 'Skill: Code Review (high effort)'
description: >-
  Effort-tier prompt for high code review — 3 angles, up to 6 candidates,
  recall-biased, up to 10 findings
ccVersion: 2.1.328
variables:
  - FORMAT_FINDINGS_LIMIT_LABEL_FN
  - MAX_FINDINGS
  - PHASE_0_GATHER_DIFF
  - CORRECTNESS_ANGLES
  - ANGLE_CONVENTIONS
  - CONVENTIONS_CANDIDATES_NOTE_FN
  - FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN
  - OUTPUT_FORMAT_FN
  - FINDING_SEVERITY_OUTPUT_OPTIONS
-->
\`high effort → 4 inline angles (bugs + conventions) → dedup (no verify) → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}\`

You are reviewing for **recall** at high effort: catch every real bug a careful
reviewer would catch in one sitting. Err on the side of surfacing.

${PHASE_0_GATHER_DIFF}
## Phase 1 — Find candidates (3 correctness angles + 1 conventions angle, up to 6 each)

Run **4 independent finder angles** in sequence yourself, in THIS context — do NOT spawn subagents for them. Each
surfaces **up to 6 candidate findings** with \`file\`, \`line\`, a short
\`summary\`, and a concrete \`failure_scenario\`.

${CORRECTNESS_ANGLES}
${ANGLE_CONVENTIONS}
${CONVENTIONS_CANDIDATES_NOTE_FN("the same")}
Pass every candidate with a nameable failure scenario through — finders that
silently drop half-believed candidates are the dominant cause of misses.

## Phase 2 — Dedup only (no verify)

Pool all candidates. Dedup near-duplicates only (same defect, same location, same reason → keep one). Do NOT run verifiers; do NOT re-judge. Give each finding that is left its \`severity\`, as Output defines it. Sort by severity.

${FORMAT_REVIEW_OUTPUT_WITH_MINIMUM_FINDINGS_FN(OUTPUT_FORMAT_FN,10)(MAX_FINDINGS,FINDING_SEVERITY_OUTPUT_OPTIONS)}
