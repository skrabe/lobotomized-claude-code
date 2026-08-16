<!--
name: 'Slash Command: /permissions — permission granted, retry allowed'
description: >-
  Same string as 19642856 on the approve path; one prompt id must cover both
  byte occurrences or an override would patch only half of them.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_0
-->
Permission granted for: ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_0.join(", ")}. You may now retry ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_0.length===1?"this command":"these commands"} if you would like.
