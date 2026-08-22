<!--
name: Plan Mode Sparse End-Turn Tools
description: >-
  Sparse-form plan-mode reminder telling the model which tools may end the turn
  and to never request plan approval via text.
ccVersion: 2.1.239
variables:
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_END_TURN_TOOLS_VAR_0
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_END_TURN_TOOLS_VAR_1
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_END_TURN_TOOLS_VAR_2
-->
End turns with ${SYSTEM_REMINDER_PLAN_MODE_SPARSE_END_TURN_TOOLS_VAR_0} (for clarifications) or ${SYSTEM_REMINDER_PLAN_MODE_SPARSE_END_TURN_TOOLS_VAR_1} (for plan approval)${SYSTEM_REMINDER_PLAN_MODE_SPARSE_END_TURN_TOOLS_VAR_2}. Never ask about plan approval via text or AskUserQuestion.
