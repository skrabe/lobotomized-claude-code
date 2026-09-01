<!--
name: Orphaned background workflow notice
description: >-
  Notification injected into model context on resume about a background workflow
  with no completion record from the previous session.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_ORPHANED_WORKFLOW_VAR_0
  - SYSTEM_REMINDER_ORPHANED_WORKFLOW_VAR_1
-->
No completion record was found for background workflow${SYSTEM_REMINDER_ORPHANED_WORKFLOW_VAR_0} from the previous session. It may have been stopped (via the UI or TaskStop — these leave no transcript marker), or it may have been running when the previous Claude Code process exited.${SYSTEM_REMINDER_ORPHANED_WORKFLOW_VAR_1}
