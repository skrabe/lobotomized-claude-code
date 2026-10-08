<!--
name: 'Data: task notification background agents webfetch resume-only tail'
description: >-
  Tail of the orphaned background-agents notification telling the model that
  web-fetch agents have no worktree or output to check and can only be resumed
  with the messaging tool.
ccVersion: 2.1.294
variables:
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_1
-->
 ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0.length===1?"Agent":"Agents"} ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0.join(", ")} fetched web content and ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0.length===1?"has":"have"} no worktree or output to check — resume ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_0.length===1?"it":"them"} with ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RESUME_ONLY_TAIL_VAR_1} only.
