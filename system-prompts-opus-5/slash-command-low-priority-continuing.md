<!--
name: 'Slash Command: /low-priority now continuing'
description: >-
  /low-priority output confirming the session continues at lower priority until
  the limit resets, that the weekly limit still applies and responses may pause,
  and how to stop
ccVersion: 2.1.239
variables:
  - SLASH_COMMAND_LOW_PRIORITY_CONTINUING_VAR_0
  - SLASH_COMMAND_LOW_PRIORITY_CONTINUING_VAR_1
-->
Continuing now at lower priority${SLASH_COMMAND_LOW_PRIORITY_CONTINUING_VAR_0?` until your limit resets at ${SLASH_COMMAND_LOW_PRIORITY_CONTINUING_VAR_0}`:" until your limit resets"}. Your weekly limit still applies, and responses may pause while waiting for spare capacity. Run /${SLASH_COMMAND_LOW_PRIORITY_CONTINUING_VAR_1} to stop.
