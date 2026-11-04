<!--
name: 'Slash Command: Clear network tool stays off until restart'
description: >-
  Output of /clear when sandbox networking prevents a tool from turning on until
  Claude Code is restarted
ccVersion: 2.1.318
variables:
  - SLASH_COMMAND_CLEAR_NETWORK_TOOL_STAYS_OFF_UNTIL_RESTART_VAR_0
  - SLASH_COMMAND_CLEAR_NETWORK_TOOL_STAYS_OFF_UNTIL_RESTART_VAR_1
-->
${SLASH_COMMAND_CLEAR_NETWORK_TOOL_STAYS_OFF_UNTIL_RESTART_VAR_0} stays off until you quit Claude Code: the sandbox has already set up the ordinary tools' network access in a way that ${SLASH_COMMAND_CLEAR_NETWORK_TOOL_STAYS_OFF_UNTIL_RESTART_VAR_1} can't use. To use ${SLASH_COMMAND_CLEAR_NETWORK_TOOL_STAYS_OFF_UNTIL_RESTART_VAR_1}, quit and start Claude Code again.
