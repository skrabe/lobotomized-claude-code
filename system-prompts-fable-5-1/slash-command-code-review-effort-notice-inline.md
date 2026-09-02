<!--
name: 'Slash Command: Code Review Effort Notice (Inline Run)'
description: >-
  Parenthetical instruction prepended to the inline /code-review prompt telling
  the model to state the effort level to the user in one short line as it
  begins.
ccVersion: 2.1.224
variables:
  - SLASH_COMMAND_CODE_REVIEW_EFFORT_NOTICE_INLINE_VAR_0
  - SLASH_COMMAND_CODE_REVIEW_EFFORT_NOTICE_INLINE_VAR_1
-->
(${SLASH_COMMAND_CODE_REVIEW_EFFORT_NOTICE_INLINE_VAR_0} Say this in one short line as you begin, including that ${SLASH_COMMAND_CODE_REVIEW_EFFORT_NOTICE_INLINE_VAR_1}.)
