<!--
name: Resume all agents or check their output
description: 'Mixed-launch variant of that guidance line, adding the worktree/output check.'
ccVersion: 2.1.232
variables:
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_RESUME_ALL_OR_CHECK_VAR_0
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_RESUME_ALL_OR_CHECK_VAR_1
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_RESUME_ALL_OR_CHECK_VAR_2
-->
Resume any of them by sending a message to its id with SendMessage, or check its worktree/output for partial work before assuming the task landed.${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_RESUME_ALL_OR_CHECK_VAR_0.length>0?` ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_RESUME_ALL_OR_CHECK_VAR_1} no worktree or output to check — resume ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_RESUME_ALL_OR_CHECK_VAR_2} with SendMessage only.`:""}
