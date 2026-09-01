<!--
name: 'Skill: Code Review (medium effort)'
description: >-
  Effort-tier prompt for medium code review — 3 angles, up to 6 candidates,
  precision-biased, up to 8 findings
ccVersion: 2.1.219
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
You are reviewing for **precision** at medium effort: every finding you surface
should be one a maintainer would act on.

Precision here means verified, not downgraded. A defect you confirmed stays a
finding at full severity — name it a bug, not a convention or a deliberate
design decision.
