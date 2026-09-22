<!--
name: 'System Reminder: Plan mode is active'
description: >-
  Reminds Claude that plan mode is active, clarifications should use
  AskUserQuestion, plans should use ExitPlanMode, and edits are not allowed
ccVersion: 2.1.178
variables:
  - ENTER_PLAN_MODE_RESULT_MESSAGE
  - ASK_USER_QUESTION_TOOL_NAME
  - EXIT_PLAN_MODE_TOOL_NAME
-->
${ENTER_PLAN_MODE_RESULT_MESSAGE}

Plan mode is read-only — don't write or edit files yet. Explore the codebase and design an approach, using ${ASK_USER_QUESTION_TOOL_NAME} to clarify intent. When ready, present the plan with ${EXIT_PLAN_MODE_TOOL_NAME}.
