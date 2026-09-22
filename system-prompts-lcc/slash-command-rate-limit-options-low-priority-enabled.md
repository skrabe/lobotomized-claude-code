<!--
name: 'Slash Command: Rate Limit Options Low Priority Enabled'
description: >-
  local-jsx onDone stdout when the user enables lower-priority mode from
  /rate-limit-options.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_RATE_LIMIT_OPTIONS_LOW_PRIORITY_ENABLED_VAR_0
  - SLASH_COMMAND_RATE_LIMIT_OPTIONS_LOW_PRIORITY_ENABLED_VAR_1
  - SLASH_COMMAND_RATE_LIMIT_OPTIONS_LOW_PRIORITY_ENABLED_VAR_2
-->
${SLASH_COMMAND_RATE_LIMIT_OPTIONS_LOW_PRIORITY_ENABLED_VAR_0==="resumed"?`Lower-priority mode is back on ${SLASH_COMMAND_RATE_LIMIT_OPTIONS_LOW_PRIORITY_ENABLED_VAR_1}`:`Continuing now at lower priority ${SLASH_COMMAND_RATE_LIMIT_OPTIONS_LOW_PRIORITY_ENABLED_VAR_1}`}. Your weekly limit still applies, and responses may pause while waiting for spare capacity. Run /${SLASH_COMMAND_RATE_LIMIT_OPTIONS_LOW_PRIORITY_ENABLED_VAR_2} to stop.
