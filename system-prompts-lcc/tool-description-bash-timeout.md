<!--
name: 'Tool Description: Bash (timeout)'
description: 'Bash tool instruction: optional timeout configuration'
ccVersion: 2.1.285
variables:
  - MAX_TIMEOUT_MS_FN
  - DEFAULT_TIMEOUT_MS_FN
-->
You may specify an optional timeout in milliseconds (up to ${MAX_TIMEOUT_MS_FN()}ms / ${MAX_TIMEOUT_MS_FN()/60000} minutes for a foreground command). By default, your command will timeout after ${DEFAULT_TIMEOUT_MS_FN()}ms (${DEFAULT_TIMEOUT_MS_FN()/60000} minutes).
