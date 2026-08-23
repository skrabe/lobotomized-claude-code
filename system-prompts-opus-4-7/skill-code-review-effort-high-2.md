<!--
name: 'Skill: Code Review (high effort)'
description: >-
  Effort-tier prompt for high code review — 3 angles, up to 6 candidates,
  recall-biased, up to 10 findings
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
  - PHASE_2_VERIFY_RECALL_BIASED
  - OUTPUT_FORMAT_FN
-->
You are reviewing for **recall** at high effort: catch every real bug a careful
reviewer would catch in one sitting.
