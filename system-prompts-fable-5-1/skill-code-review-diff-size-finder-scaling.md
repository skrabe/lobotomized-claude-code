<!--
name: Code Review Diff-Size Finder Scaling
description: >-
  Model-facing code-review prompt fragment telling the review agent roughly how
  many finder subagents to spawn based on the diff line count.
ccVersion: 2.1.202
variables:
  - SKILL_CODE_REVIEW_DIFF_SIZE_FINDER_SCALING_VAR_0
  - SKILL_CODE_REVIEW_DIFF_SIZE_FINDER_SCALING_VAR_1
-->
This diff is about ${SKILL_CODE_REVIEW_DIFF_SIZE_FINDER_SCALING_VAR_0} lines. Spawn about ${SKILL_CODE_REVIEW_DIFF_SIZE_FINDER_SCALING_VAR_1} finder subagents (min 2, max 8) — scale your investigation depth to the diff size rather than using a fixed large fleet.

