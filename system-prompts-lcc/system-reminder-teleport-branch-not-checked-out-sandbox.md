<!--
name: 'System Reminder: Teleport branch not checked out (sandbox)'
description: >-
  Appended to the continued-from-another-machine meta message when the cloud
  session's branch wasn't checked out because the sandbox may be on, telling the
  model not to switch itself.
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_TELEPORT_BRANCH_NOT_CHECKED_OUT_SANDBOX_VAR_0
  - SYSTEM_REMINDER_TELEPORT_BRANCH_NOT_CHECKED_OUT_SANDBOX_VAR_1
-->


The cloud session's branch ${SYSTEM_REMINDER_TELEPORT_BRANCH_NOT_CHECKED_OUT_SANDBOX_VAR_0(SYSTEM_REMINDER_TELEPORT_BRANCH_NOT_CHECKED_OUT_SANDBOX_VAR_1.branch)} was not checked out, because Claude Code's sandbox may be on here, so this folder may lack that session's work. The user was shown how to switch to it. Do not fetch that branch or switch to it yourself; if the task needs it and git shows another branch, ask the user to switch in their own terminal.
