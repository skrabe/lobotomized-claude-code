<!--
name: Plan Mode Sparse Continuation Reminder
description: >-
  Model-facing system-reminder (L9m, injected via _p([On({content,isMeta:!0})]))
  re-asserting plan-mode constraints on plan-continuation turns; gated by
  reminderType sparse.
ccVersion: 2.1.191
variables:
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_0
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_1
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_2
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_3
-->

Plan mode still active (see full instructions earlier in conversation). Read-only except plan file (${SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_0.planFilePath})${SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_1}. ${SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_2} ${SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_3({workshopActive:SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_VAR_0.workshopActiveDocPath!==void 0,form:"sparse"})}
