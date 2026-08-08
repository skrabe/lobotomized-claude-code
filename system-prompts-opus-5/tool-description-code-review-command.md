<!--
name: 'Tool Description: Code review command'
description: >-
  Describes the code review command and its effort levels, PR comment mode, and
  fix mode; injected as the model-facing description of the /code-review slash
  command.
ccVersion: 2.1.224
variables:
  - IS_CLOUD_CODE_REVIEW_ENABLED_FN
  - HAS_CLAUDE_AI_ACCESS_FN
-->
Review the current diff, or a PR number/branch/path target, for correctness bugs and reuse/simplification/efficiency cleanups at the given effort level (low/medium: fewer, high-confidence findings; high→max: broader coverage, may include uncertain findings${IS_CLOUD_CODE_REVIEW_ENABLED_FN()?`; ultra: deep multi-agent review in the cloud${HAS_CLAUDE_AI_ACCESS_FN()?"":" (requires claude.ai account access)"}`:""}); with no level given, it reuses the level you typed last. Pass --comment to post findings as inline PR comments, or --fix to apply the findings to the working tree after the review.
