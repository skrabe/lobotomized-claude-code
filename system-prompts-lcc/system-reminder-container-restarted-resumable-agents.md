<!--
name: 'System Reminder: Container restarted resumable agents'
description: >-
  After a container restart, lists the stopped built-in agents that can be
  resumed by messaging their agent id with the send-message tool, followed by
  the lost-task note
ccVersion: 2.1.322
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_0
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_1
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_2
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_3
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_4
-->
${SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_0.length===0?"Only these stopped agents":"Of the others, only these stopped agents"} can be resumed: ${SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_1.join(", ")}. To resume one, send a message to its agent id (agent names no longer resolve after a restart) with the ${SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_2} tool instead of re-creating it: it continues from its saved transcript${SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_3}. If no transcript is found the resume fails; re-create the agent then. ${SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_4}
