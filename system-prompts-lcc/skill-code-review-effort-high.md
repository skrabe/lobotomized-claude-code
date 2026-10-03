<!--
name: 'Skill: Code Review (high effort)'
description: >-
  Effort-tier prompt for high code review — 3+5 angles, up to 6 candidates,
  recall-biased verify, up to 10 findings
ccVersion: 2.1.288
variables:
  - FORMAT_FINDINGS_LIMIT_LABEL_FN
  - MAX_FINDINGS
  - PHASE_0_GATHER_DIFF
  - AGENT_TOOL_NAME
  - AGENT_UNAVAILABLE_INSTRUCTIONS
  - BASE_FINDER_ANGLES_BLOCK
  - CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE
  - RECALL_BIASED_VERIFY_PHASE
  - OUTPUT_FORMAT_FN
-->
\`high effort → 3+5 angles × 6 candidates → 1-vote verify (recall-biased) → ${FORMAT_FINDINGS_LIMIT_LABEL_FN(MAX_FINDINGS)}\`

You are reviewing for **recall** at high effort: catch every real bug a careful
reviewer would catch in one sitting. Err on the side of surfacing.

${PHASE_0_GATHER_DIFF}
## Phase 1 — Find candidates (3 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 6 each)

Run **8 independent finder angles** via the ${AGENT_TOOL_NAME} tool. Each
surfaces **up to 6 candidate findings** with \`file\`, \`line\`, a one-line
\`summary\`, and a concrete \`failure_scenario\`. ${AGENT_UNAVAILABLE_INSTRUCTIONS}

${BASE_FINDER_ANGLES_BLOCK}
${CLEANUP_AND_ALTITUDE_CANDIDATES_NOTE}
Pass every candidate with a nameable failure scenario through — finders that
silently drop half-believed candidates bypass the verify step and are the
dominant cause of misses.

${RECALL_BIASED_VERIFY_PHASE}
${OUTPUT_FORMAT_FN(MAX_FINDINGS)}
