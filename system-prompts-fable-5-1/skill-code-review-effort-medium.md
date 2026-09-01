<!--
name: 'Skill: Code Review (medium effort)'
description: >-
  Effort-tier prompt for medium code review — 3 angles, up to 6 candidates,
  precision-biased, up to 8 findings
ccVersion: 2.1.218
variables:
  - PHASE_0_GATHER_DIFF
  - AGENT_TOOL_NAME
  - ANGLES_LINE_BY_LINE
  - ANGLE_REUSE
  - ANGLE_SIMPLIFICATION
  - ANGLE_EFFICIENCY
  - ANGLE_ALTITUDE
  - ANGLE_CONVENTIONS
  - CLEANUP_CANDIDATES_NOTE
  - PHASE_2_VERIFY_3_STATE
  - OUTPUT_FORMAT_FN
-->
\`medium effort → 3+5 angles × 6 candidates → 1-vote verify → ≤8 findings\`

You are reviewing for **precision** at medium effort: every finding you surface
should be one a maintainer would act on.

${PHASE_0_GATHER_DIFF}
## Phase 1 — Find candidates (3 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 6 each)

Run **8 independent finder angles** via the ${AGENT_TOOL_NAME} tool. Each
surfaces **up to 6 candidate findings** with \`file\`, \`line\`, a one-line
\`summary\`, and a concrete \`failure_scenario\`. ${ANGLES_LINE_BY_LINE}

${ANGLE_REUSE}
${ANGLE_SIMPLIFICATION}
Pass every candidate with a nameable failure scenario through — dropping
half-believed candidates bypasses the verify step.

${ANGLE_EFFICIENCY}
${ANGLE_ALTITUDE(8)}
