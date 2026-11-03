<!--
name: 'System Reminder: Plan mode Doc approval (sparse)'
description: >-
  Sparse plan-mode reminder for plans kept in a Claude Doc: call the exit tool
  with no argument and never ask about approval via text or the ask tool
ccVersion: 2.1.317
variables:
  - SYSTEM_REMINDER_PLAN_MODE_DOC_APPROVAL_SPARSE_VAR_0
  - SYSTEM_REMINDER_PLAN_MODE_DOC_APPROVAL_SPARSE_VAR_1
-->
When the Doc holds the final plan, call ${SYSTEM_REMINDER_PLAN_MODE_DOC_APPROVAL_SPARSE_VAR_0} with no argument. Never ask about plan approval via text or ${SYSTEM_REMINDER_PLAN_MODE_DOC_APPROVAL_SPARSE_VAR_1}.
