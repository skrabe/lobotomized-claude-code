<!--
name: Dir Sync Too Large On Laptop
description: >-
  Model reminder that files in the user's directory are larger than sync carries
  and will never arrive in this checkout.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_TOO_LARGE_ON_LAPTOP_VAR_0
-->
Directory sync: ${SYSTEM_REMINDER_DIR_SYNC_TOO_LARGE_ON_LAPTOP_VAR_0} ${SYSTEM_REMINDER_DIR_SYNC_TOO_LARGE_ON_LAPTOP_VAR_0===1?"file":"files"} in the user's directory ${SYSTEM_REMINDER_DIR_SYNC_TOO_LARGE_ON_LAPTOP_VAR_0===1?"is":"are"} larger than sync carries and will never arrive in this checkout (the user was told which); say so if they matter to the task rather than treating the directory as complete.
