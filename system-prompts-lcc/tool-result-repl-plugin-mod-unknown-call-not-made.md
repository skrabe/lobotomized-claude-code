<!--
name: 'Tool result: REPL plugin mod unknown call not made'
description: >-
  Tool result refusing a tool call from code when Claude Code could not tell
  whether a plugin mod checks tool calls
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_PLUGIN_MOD_UNKNOWN_CALL_NOT_MADE_VAR_0
  - TOOL_RESULT_REPL_PLUGIN_MOD_UNKNOWN_CALL_NOT_MADE_VAR_1
-->
This call was not made. Claude Code could not find out whether an installed plugin is a mod (a plugin with JavaScript hooks) that checks tool calls, and ${TOOL_RESULT_REPL_PLUGIN_MOD_UNKNOWN_CALL_NOT_MADE_VAR_0} does not yet support that for a tool call that your code makes. Do not look for another way to do the same thing. Tell the user that they can try again, ${TOOL_RESULT_REPL_PLUGIN_MOD_UNKNOWN_CALL_NOT_MADE_VAR_1}
