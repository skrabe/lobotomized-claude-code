<!--
name: 'Tool result: deferred tool unavailable call dropped (join)'
description: >-
  Join of the dropped-deferred-call message and the optional note that the
  calling script was stopped; sent as an is_error tool_result.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_DEFERRED_TOOL_UNAVAILABLE_CALL_DROPPED_JOIN_VAR_0
  - TOOL_RESULT_DEFERRED_TOOL_UNAVAILABLE_CALL_DROPPED_JOIN_VAR_1
-->
${TOOL_RESULT_DEFERRED_TOOL_UNAVAILABLE_CALL_DROPPED_JOIN_VAR_0}${TOOL_RESULT_DEFERRED_TOOL_UNAVAILABLE_CALL_DROPPED_JOIN_VAR_1.script===void 0?"":" The script that made it was stopped there, and its earlier calls may have run."}
