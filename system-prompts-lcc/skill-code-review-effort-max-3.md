<!--
name: 'Skill: Code Review (max / xhigh effort)'
description: >-
  Effort-tier prompt for max and xhigh code review — 5 angles, up to 8
  candidates, recall-biased, up to 15 findings
ccVersion: 2.1.288
variables:
  - EFFORT_LEVEL
  - FORMAT_FINDINGS_LIMIT_LABEL_FN
  - MAX_FINDINGS
  - PHASE_0_GATHER_DIFF
  - AGENT_TOOL_NAME
  - AGENT_UNAVAILABLE_INSTRUCTIONS
  - EXTENDED_FINDER_ANGLES_BLOCK
  - CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE
  - THREE_STATE_VERIFY_PHASE
  - GAP_SWEEP_PHASE
  - OUTPUT_FORMAT_FN
-->
\`${EFFORT_LEVEL} effort → 5+5 angles × 8 candidates → 1-vote verify → sweep → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}\`

You are reviewing for **recall** at ${EFFORT_LEVEL==="max"?"maximum":"extra-high"} effort: catch every real bug. At
this level, catching real bugs matters more than avoiding false positives.
Err on the side of surfacing.

${PHASE_0_GATHER_DIFF}
## Phase 1 — Find candidates (5 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 8 each)

Run **10 independent finder angles** via the ${AGENT_TOOL_NAME} tool. Each
surfaces **up to 8 candidate findings**. Do NOT let one angle's conclusions
suppress another's — if two angles flag the same line for different reasons,
record both. ${AGENT_UNAVAILABLE_INSTRUCTIONS}

${EXTENDED_FINDER_ANGLES_BLOCK}
${CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE}
${THREE_STATE_VERIFY_PHASE}
This is recall mode — a single non-REFUTED vote carries the finding. Do NOT
drop on uncertainty.

${GAP_SWEEP_PHASE}
${OUTPUT_FORMAT_FN(MAX_FINDINGS)}
