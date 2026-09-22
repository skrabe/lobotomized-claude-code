<!--
name: 'System Reminder: Directory sync checkout update unfinished'
description: >-
  dir_sync_notice wrapping apply residue to tell the model the cloud checkout
  could not finish updating from the user's machine.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_UPDATE_UNFINISHED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_UPDATE_UNFINISHED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_UPDATE_UNFINISHED_VAR_2
  - SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_UPDATE_UNFINISHED_VAR_3
-->
Directory sync could not finish updating this checkout from the user's machine: ${SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_UPDATE_UNFINISHED_VAR_0(SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_UPDATE_UNFINISHED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_UPDATE_UNFINISHED_VAR_2.residue.join("; ")),SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_UPDATE_UNFINISHED_VAR_3)}.
