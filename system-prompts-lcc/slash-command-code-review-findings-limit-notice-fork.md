<!--
name: 'Slash Command: Code Review Findings Limit Notice Fork'
description: >-
  Parenthetical prepended to the forked /code-review prompt telling the model to
  open its report with one line telling the user about the findings-limit note,
  with an optional how-to-reset clause.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_FORK_VAR_0
  - SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_FORK_VAR_1
-->
(${SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_FORK_VAR_0} Open your report with one short line telling the user this${SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_FORK_VAR_1?`, and that ${SLASH_COMMAND_CODE_REVIEW_FINDINGS_LIMIT_NOTICE_FORK_VAR_1}`:""}; that opening line reaches them with the findings.)

