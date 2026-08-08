<!--
name: 'System Reminder: Fork-Source Live Parent'
description: >-
  System reminder injected as a task notification at the start of a forked
  session, telling the model it is a copy of a still-running parent session and
  how to coordinate with it.
ccVersion: 2.1.224
variables:
  - SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_0
  - SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_1
  - SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_2
  - SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_3
  - SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_4
  - SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_5
-->
<${SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_0}>
<${SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_1}>
This session began as a fork (copy) of another session that is still running: ${SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_2}. The conversation up to ${SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_3} is shared history with it; the two sessions have since diverged, and neither sees the other's new activity. To coordinate with it — hand results back, ask what it has done since, avoid duplicating its work — ${SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_4} and message it with ${SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_5}.
</${SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_1}>
</${SYSTEM_REMINDER_FORK_SOURCE_LIVE_PARENT_VAR_0}>
