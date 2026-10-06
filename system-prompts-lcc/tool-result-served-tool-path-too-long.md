<!--
name: 'Tool Result: Served tool path too long'
description: >-
  Refusal returned to a cloud session's tool call when the path's full length
  exceeds what the operating system accepts; nothing was read or written
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_SERVED_TOOL_PATH_TOO_LONG_VAR_0
  - TOOL_RESULT_SERVED_TOOL_PATH_TOO_LONG_VAR_1
-->
${TOOL_RESULT_SERVED_TOOL_PATH_TOO_LONG_VAR_0} cannot open this path: written out in full it comes to ${TOOL_RESULT_SERVED_TOOL_PATH_TOO_LONG_VAR_1.toLocaleString("en-US")} bytes or more, and its operating system takes no path that long. Nothing was read or written.
