<!--
name: Code Review After The Review Section
description: >-
  Model-facing prompt section appended to the code-review skill instructing the
  model to invoke /verify after reporting findings when the diff has a runtime
  surface.
ccVersion: 2.1.202
variables:
  - SKILL_CODE_REVIEW_AFTER_THE_REVIEW_VAR_0
-->


## After the review

After the findings are reported (and applied, when --fix was passed): if \`/${SKILL_CODE_REVIEW_AFTER_THE_REVIEW_VAR_0}\` has NOT run this session and the diff has a runtime surface (not test-only or docs-only per the pre-ship exemptions), invoke \`/${SKILL_CODE_REVIEW_AFTER_THE_REVIEW_VAR_0}\` now — this review checks that the diff reads right; \`/${SKILL_CODE_REVIEW_AFTER_THE_REVIEW_VAR_0}\` checks that it runs right. State which you did.
