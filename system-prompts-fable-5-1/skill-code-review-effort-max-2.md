<!--
name: 'Skill: Code Review (max / xhigh effort, recall posture)'
description: >-
  Effort-tier posture fragment for max / xhigh code review — recall over
  precision. Shrunk to this fragment in 2.1.214; the phases and finder angles
  now live in skill-code-review-effort-max and -max-3.
ccVersion: 2.1.218
variables:
  - EFFORT_LEVEL
-->
You are reviewing for **recall** at ${EFFORT_LEVEL==="max"?"maximum":"extra-high"} effort: catch every real bug. At
this level, catching real bugs matters more than avoiding false positives.
Err on the side of surfacing.
