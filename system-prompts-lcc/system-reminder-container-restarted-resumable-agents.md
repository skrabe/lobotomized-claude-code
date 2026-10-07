<!--
name: 'System Reminder: Container restarted resumable agents'
description: >-
  After a container restart, lists the stopped built-in agents that can be
  resumed by messaging their agent id with the send-message tool, and says every
  other stopped task is lost
ccVersion: 2.1.292
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_0
  - SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_1
-->
Only these stopped agents can be resumed: ${SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_0.join(", ")}. To resume one, send a message to its agent id (agent names no longer resolve after a restart) with the ${SYSTEM_REMINDER_CONTAINER_RESTARTED_RESUMABLE_AGENTS_VAR_1} tool instead of re-creating it: it continues from its saved transcript, as a general-purpose agent with the same tools if its saved settings did not survive the restart. If no transcript is found the resume fails; re-create the agent then. Every other stopped task listed here is lost: do not send a message to its id.
