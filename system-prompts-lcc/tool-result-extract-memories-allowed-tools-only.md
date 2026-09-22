<!--
name: 'Tool Result: Extract Memories Allowed Tools Only'
description: >-
  Permission deny telling the extract_memories pass it may only call the listed
  tools.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_EXTRACT_MEMORIES_ALLOWED_TOOLS_ONLY_VAR_0
-->
this background memory pass may only call ${[...TOOL_RESULT_EXTRACT_MEMORIES_ALLOWED_TOOLS_ONLY_VAR_0].join(", ")}
