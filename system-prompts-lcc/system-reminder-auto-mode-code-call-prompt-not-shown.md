<!--
name: 'System Reminder: Auto mode code call approval prompt not shown'
description: >-
  Explains a code-issued call needing approval was skipped because an earlier
  permission prompt went unanswered, forbids workarounds and asks the model to
  report the skipped step
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_AUTO_MODE_CODE_CALL_PROMPT_NOT_SHOWN_VAR_0
-->
${SYSTEM_REMINDER_AUTO_MODE_CODE_CALL_PROMPT_NOT_SHOWN_VAR_0}It needs the user's approval, and it was not put to them, because an earlier permission prompt went unanswered. Such prompts are shown again once the user types something. Do not get the same effect another way to avoid the approval. Go on with other work and tell the user which step was skipped and still needs their approval.
