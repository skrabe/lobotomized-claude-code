<!--
name: 'System Reminder: Directory sync stopped checkout kept'
description: >-
  Tells Claude that file sync with the user's attached machine stopped (with the
  reason) while this checkout stays unchanged and its own, that the two folders
  are now separate copies, and to tell the user if that matters
ccVersion: 2.1.277
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_STOPPED_CHECKOUT_KEPT_VAR_0
  - SYSTEM_REMINDER_DIRECTORY_SYNC_STOPPED_CHECKOUT_KEPT_VAR_1
-->
File sync with the user's attached machine has stopped for this session: ${SYSTEM_REMINDER_DIRECTORY_SYNC_STOPPED_CHECKOUT_KEPT_VAR_0(SYSTEM_REMINDER_DIRECTORY_SYNC_STOPPED_CHECKOUT_KEPT_VAR_1)}. This checkout is unchanged — nothing was removed or set aside — and it stays this session's own: keep working in it, and commit and push your work as usual. The user's folder on their machine keeps its files too; from here on it is a separate copy that changes here do not reach, and changes there do not arrive here. Tell the user if that matters for the task.
