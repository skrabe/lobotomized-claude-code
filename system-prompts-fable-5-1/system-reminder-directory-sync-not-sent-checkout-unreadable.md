<!--
name: 'System Reminder: Directory Sync Not Sent Checkout Unreadable'
description: >-
  Reminds the model that this turn's changes were not sent because sync will not
  read the checkout as it stands.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_NOT_SENT_CHECKOUT_UNREADABLE_VAR_0
  - SYSTEM_REMINDER_DIRECTORY_SYNC_NOT_SENT_CHECKOUT_UNREADABLE_VAR_1
-->
Directory sync: this turn's changes were NOT sent to the user's machine because sync will not read this checkout as it stands: ${SYSTEM_REMINDER_DIRECTORY_SYNC_NOT_SENT_CHECKOUT_UNREADABLE_VAR_0(SYSTEM_REMINDER_DIRECTORY_SYNC_NOT_SENT_CHECKOUT_UNREADABLE_VAR_1)}. Nothing of yours reaches the user until that is fixed (sync tries again after every turn); fix it and tell the user.
