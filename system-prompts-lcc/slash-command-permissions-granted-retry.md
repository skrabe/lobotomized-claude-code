<!--
name: 'Slash command: /permissions granted retry'
description: >-
  Meta message telling the model permission was granted only for the exact
  commands or calls listed and it may retry them
ccVersion: 2.1.314
variables:
  - SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_0
  - SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_1
  - SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_2
  - SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_3
-->
Permission granted for ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_0} only, ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_1?"as one whole string":"each as one whole string"}: ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_2.join(", ")}. This does not approve any other ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_3}, any part of ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_1?"this one":"these"}, or running ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_1?"it":"them"} with added options such as turning off the sandbox, extra network access, or running in the background. You may now retry ${SLASH_COMMAND_PERMISSIONS_GRANTED_RETRY_VAR_0} if you would like.
