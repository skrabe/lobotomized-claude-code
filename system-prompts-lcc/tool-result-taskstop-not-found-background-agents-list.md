<!--
name: 'Tool Result: TaskStop not found, background agents list'
description: >-
  Suffix listing background agents running or waiting when a TaskStop id is not
  found
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_TASKSTOP_NOT_FOUND_BACKGROUND_AGENTS_LIST_VAR_0
-->
. Background agents running or waiting: ${TOOL_RESULT_TASKSTOP_NOT_FOUND_BACKGROUND_AGENTS_LIST_VAR_0.join(", ")}
