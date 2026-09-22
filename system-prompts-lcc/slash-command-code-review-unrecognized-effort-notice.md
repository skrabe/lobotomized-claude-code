<!--
name: 'Slash Command: Code Review Unrecognized Effort Notice'
description: >-
  Notice injected into the /code-review prompt when the user typed an effort
  level the command does not recognize, naming the valid levels and the level
  actually used.
ccVersion: 2.1.224
variables:
  - SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_0
  - SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_1
  - SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_2
  - SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_3
-->
Ignoring unrecognized effort "${SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_0}"; valid: ${SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_1.join(", ")}. Using ${SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_2}${SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_3===SLASH_COMMAND_CODE_REVIEW_UNRECOGNIZED_EFFORT_NOTICE_VAR_2?", the level the user typed last time":""}.
