<!--
name: 'Tool Result: ExitWorktree not removed for connector files'
description: >-
  Thrown ExitWorktree error saying the worktree was not removed and the session
  remains in it because of connector-saved files
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_CONNECTOR_FILES_VAR_0
  - TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_CONNECTOR_FILES_VAR_1
  - TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_CONNECTOR_FILES_VAR_2
-->
Worktree not removed; the session is still in it. ${TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_CONNECTOR_FILES_VAR_0==="unknown"?`Its ${TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_CONNECTOR_FILES_VAR_1} folder could not be checked, and may hold files saved from connectors that removing the worktree would delete.`:`Its ${TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_CONNECTOR_FILES_VAR_1} folder now holds files saved from connectors that removing the worktree would delete.`} ${TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_CONNECTOR_FILES_VAR_2}
