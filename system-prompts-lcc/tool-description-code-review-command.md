<!--
name: 'Tool Description: Code review command'
description: >-
  Describes the code review command and its effort levels, PR comment mode, and
  fix mode; injected as the model-facing description of the /code-review slash
  command.
ccVersion: 2.1.288
variables:
  - IS_CLOUD_CODE_REVIEW_ENABLED_FN
  - HAS_CLAUDE_AI_ACCESS_FN
-->
Review the current diff, or a PR number/branch/path target, for correctness bugs (plus reuse/simplification/efficiency cleanups where the model's review recipe covers them) at the given effort level (low/medium: fewer, high-confidence findings; high→max: broader coverage, may include uncertain findings${IS_CLOUD_CODE_REVIEW_ENABLED_FN}); with no level given, it reuses the level you typed last. Pass --comment to post findings as inline PR comments, or --fix to apply the findings to the working tree after the review. Pass --max-findings <n> to report up to n findings, or --max-findings all for every finding. The choice stays until you pass --max-findings default.${HAS_CLAUDE_AI_ACCESS_FN}
