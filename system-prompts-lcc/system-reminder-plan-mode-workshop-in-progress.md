<!--
name: Plan Mode Workshop In Progress
description: >-
  Block appended to the full plan-mode system reminder when a decision workshop
  is active, restating the grant and to fold decisions back into the plan file.
ccVersion: 2.1.219
variables:
  - SYSTEM_REMINDER_PLAN_MODE_WORKSHOP_IN_PROGRESS_VAR_0
  - SYSTEM_REMINDER_PLAN_MODE_WORKSHOP_IN_PROGRESS_VAR_1
-->


A decision workshop is in progress for this session — ${SYSTEM_REMINDER_PLAN_MODE_WORKSHOP_IN_PROGRESS_VAR_0(SYSTEM_REMINDER_PLAN_MODE_WORKSHOP_IN_PROGRESS_VAR_1.workshopActiveDocPath,{form:"full",mode:"active"})} Fold each resolved decision back into the plan file as the workshop progresses.
