<!--
name: Orphaned background agent (already completed) notice
description: >-
  Notification injected into model context on resume about a background agent
  that had completed but lost only its notification.
ccVersion: 2.1.294
variables:
  - SYSTEM_REMINDER_ORPHANED_AGENT_COMPLETED_VAR_0
-->
It had already completed before the previous Claude Code process exited — only its completion notification was lost, so it was not restarted and no further task notification will arrive. ${SYSTEM_REMINDER_ORPHANED_AGENT_COMPLETED_VAR_0}
