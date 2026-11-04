<!--
name: 'Tool Description: REPL permission mode sync wait'
description: >-
  Notes that in permission-asking modes each REPL call waits for its script and
  the script time limit includes prompts
ccVersion: 2.1.318
variables:
  - TOOL_DESCRIPTION_REPL_PERMISSION_MODE_SYNC_WAIT_VAR_0
-->

The user can change the permission mode at any time. In a mode that asks for permission, every \`REPL\` call instead waits for its script and returns its output. The script is stopped ${TOOL_DESCRIPTION_REPL_PERMISSION_MODE_SYNC_WAIT_VAR_0} ms after it starts, and that time includes time spent waiting at permission prompts.
