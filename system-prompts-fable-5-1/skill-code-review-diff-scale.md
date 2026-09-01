<!--
name: Code-review diff-scale sizing note
description: >-
  Code-review prompt fragment telling the model how many finder subagents to
  spawn based on committed diff size.
ccVersion: 2.1.206
variables:
  - SKILL_CODE_REVIEW_DIFF_SCALE_VAR_0
  - SKILL_CODE_REVIEW_DIFF_SCALE_VAR_1
-->
The committed diff (@{upstream}...HEAD) is about ${SKILL_CODE_REVIEW_DIFF_SCALE_VAR_0} lines. Uncommitted changes aren't counted here, so treat this as a floor — start with about ${SKILL_CODE_REVIEW_DIFF_SCALE_VAR_1} finder subagents (min 2, max 8) and scale up if Phase 0 finds additional working-tree scope.

