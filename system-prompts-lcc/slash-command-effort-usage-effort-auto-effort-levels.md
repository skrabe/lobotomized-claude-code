<!--
name: /effort usage and available effort levels
description: /effort usage header and the effort levels heading
ccVersion: 2.1.314
variables:
  - SLASH_COMMAND_EFFORT_USAGE_EFFORT_AUTO_EFFORT_LEVELS_VAR_0
  - SLASH_COMMAND_EFFORT_USAGE_EFFORT_AUTO_EFFORT_LEVELS_VAR_1
-->
Usage: /effort [${SLASH_COMMAND_EFFORT_USAGE_EFFORT_AUTO_EFFORT_LEVELS_VAR_0.join("|")}|auto${SLASH_COMMAND_EFFORT_USAGE_EFFORT_AUTO_EFFORT_LEVELS_VAR_1?"|ultracode [on|off]":""}]

Effort levels:
