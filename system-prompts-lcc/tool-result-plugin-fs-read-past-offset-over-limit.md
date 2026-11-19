<!--
name: >-
  Tool Result: plugin $.fs.read refusal — rest of file past offset over the
  limit
description: >-
  Reason fragment of a plugin $.fs.read refusal when what follows the offset is
  over the byte limit, telling the caller to pass a length.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_PLUGIN_FS_READ_PAST_OFFSET_OVER_LIMIT_VAR_0
  - TOOL_RESULT_PLUGIN_FS_READ_PAST_OFFSET_OVER_LIMIT_VAR_1
-->
what follows offset ${TOOL_RESULT_PLUGIN_FS_READ_PAST_OFFSET_OVER_LIMIT_VAR_0} is over the ${TOOL_RESULT_PLUGIN_FS_READ_PAST_OFFSET_OVER_LIMIT_VAR_1}-byte limit; pass length
