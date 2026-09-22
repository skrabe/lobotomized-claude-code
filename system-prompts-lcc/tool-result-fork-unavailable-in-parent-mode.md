<!--
name: 'Tool Result: Fork Unavailable In Parent Mode'
description: >-
  Subagent-launch tool_result error when a fork is requested from plan or
  dontAsk mode, which the child would not inherit.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_FORK_UNAVAILABLE_IN_PARENT_MODE_VAR_0
-->
Fork is not available in ${TOOL_RESULT_FORK_UNAVAILABLE_IN_PARENT_MODE_VAR_0} mode: the fork would run without the ${TOOL_RESULT_FORK_UNAVAILABLE_IN_PARENT_MODE_VAR_0} restriction its parent has. Start a fresh context instead.
