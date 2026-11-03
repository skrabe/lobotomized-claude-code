<!--
name: Plan Mode Sparse Continuation Reminder
description: >-
  Model-facing system-reminder (L9m, injected via _p([On({content,isMeta:!0})]))
  re-asserting plan-mode constraints on plan-continuation turns; gated by
  reminderType sparse.
ccVersion: 2.1.317
variables:
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_3_VAR_0
  - SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_3_VAR_1
-->
Plan mode still active (see full instructions earlier in conversation). Read-only, ${SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_3_VAR_0!==void 0?"except for the plan's Claude Doc":"and there is no plan file"}. Follow 5-phase workflow. ${SYSTEM_REMINDER_PLAN_MODE_SPARSE_CONTINUATION_3_VAR_1("sparse")}
