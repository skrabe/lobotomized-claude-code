<!--
name: 'Tool result: computer click holds multiple non-modifier keys'
description: >-
  Computer-use validation error when a click's modifier text holds more than one
  non-modifier key.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_CLICK_CHORD_MULTIPLE_KEYS_VAR_0
  - TOOL_RESULT_COMPUTER_USE_CLICK_CHORD_MULTIPLE_KEYS_VAR_1
-->
A click may hold modifier keys and at most one other key; "${TOOL_RESULT_COMPUTER_USE_CLICK_CHORD_MULTIPLE_KEYS_VAR_0}" has ${TOOL_RESULT_COMPUTER_USE_CLICK_CHORD_MULTIPLE_KEYS_VAR_1.length} other keys. Press each with its own \`key\` action, then click.
