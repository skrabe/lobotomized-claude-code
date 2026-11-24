<!--
name: 'System reminder: container restart untold agents resume hint'
description: >-
  Resume hint for agents stopped by a container restart: resume via a message to
  the agent id instead of relaunching.
ccVersion: 2.1.331
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTART_UNTOLD_AGENTS_RESUME_HINT_VAR_0
-->
If an agent's work should go on, resume it rather than launch it again: send a message to its agent id with the ${SYSTEM_REMINDER_CONTAINER_RESTART_UNTOLD_AGENTS_RESUME_HINT_VAR_0} tool. It continues from its saved transcript, which still holds its task.
