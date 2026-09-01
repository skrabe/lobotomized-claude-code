<!--
name: 'Tool Description: EnterPlanMode'
description: >-
  Tool description for entering plan mode to explore and design implementation
  approaches
ccVersion: 2.1.215
variables:
  - ASK_USER_QUESTION_TOOL_NAME
  - CONDITIONAL_USE_AGENT_TOOL_INSTEAD_NOTE
  - WHAT_HAPPENS_IN_PLAN_MODE_FN
-->

Transition into plan mode to explore the codebase and design an implementation approach for user approval before writing code. Requires user approval to enter.

${WHAT_HAPPENS_IN_PLAN_MODE_FN()}
