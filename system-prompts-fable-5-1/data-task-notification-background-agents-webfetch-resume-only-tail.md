<!--
name: WebFetch Agents Resume With SendMessage Only
description: >-
  Tail on the multi-agent orphan notification noting WebFetch-launched agents
  have no worktree or output, so they must be resumed with SendMessage only.
ccVersion: 2.1.265
variables:
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0
-->
 ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0.length===1?"Agent":"Agents"} ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0.join(", ")} fetched web content and ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0.length===1?"has":"have"} no worktree or output to check — resume ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0.length===1?"it":"them"} with SendMessage only.
