<!--
name: 'System Reminder: Container restart agents stopped, resume them'
description: >-
  Lists agents stopped by a mid-turn container restart and tells the model to
  resume them by message rather than relaunch
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTART_AGENTS_STOPPED_RESUME_THEM_VAR_0
  - SYSTEM_REMINDER_CONTAINER_RESTART_AGENTS_STOPPED_RESUME_THEM_VAR_1
-->
The container was restarted in the middle of a turn. These agents, which you launched in that turn, are now stopped, and their results never reached you: ${SYSTEM_REMINDER_CONTAINER_RESTART_AGENTS_STOPPED_RESUME_THEM_VAR_0.join(", ")}. If you still need an agent's result, resume it rather than launch it again: send a message to its agent id with the ${SYSTEM_REMINDER_CONTAINER_RESTART_AGENTS_STOPPED_RESUME_THEM_VAR_1} tool. It continues from its saved transcript, which still holds its task. If the resume fails, launch the agent again.
