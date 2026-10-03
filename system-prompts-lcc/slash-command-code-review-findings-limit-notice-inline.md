<!--
name: 'Slash Command: Code Review Findings Limit Notice Inline'
description: >-
  Parenthetical prepended to the inline /code-review prompt telling the model to
  tell the user the findings-limit note in one short line as it begins, with an
  optional including-that clause.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_INLINE_VAR_0
  - SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_INLINE_VAR_1
-->
(${SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_INLINE_VAR_0} Tell the user this in one short line as you begin${SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_INLINE_VAR_1?`, including that ${SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_INLINE_VAR_1}`:""}.)

