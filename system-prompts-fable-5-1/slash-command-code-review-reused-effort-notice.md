<!--
name: 'Slash Command: Code Review Reused Effort Notice'
description: >-
  Notice injected into the /code-review prompt when no level was typed and the
  command reuses the level the user last chose, optionally naming the level
  actually running.
ccVersion: 2.1.224
variables:
  - SLASH_COMMAND_CODE_REVIEW_REUSED_EFFORT_NOTICE_VAR_0
  - SLASH_COMMAND_CODE_REVIEW_REUSED_EFFORT_NOTICE_VAR_1
-->
reusing ${SLASH_COMMAND_CODE_REVIEW_REUSED_EFFORT_NOTICE_VAR_0}, the level the user typed last time${SLASH_COMMAND_CODE_REVIEW_REUSED_EFFORT_NOTICE_VAR_1!==SLASH_COMMAND_CODE_REVIEW_REUSED_EFFORT_NOTICE_VAR_0?`; running at ${SLASH_COMMAND_CODE_REVIEW_REUSED_EFFORT_NOTICE_VAR_1} here`:""}
