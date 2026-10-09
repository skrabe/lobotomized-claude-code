<!--
name: Duplicate tool call refused
description: >-
  Warns that a call already started and asks to inspect its effects before
  retrying.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_DUPLICATE_CALL_NOT_RUN_AGAIN_VAR_0
-->
${TOOL_RESULT_SERVED_TOOL_DUPLICATE_CALL_NOT_RUN_AGAIN_VAR_0.name} was not run again: this very call was already started here once. It may have finished, failed or been cut off: check what it did before you send a new call.
