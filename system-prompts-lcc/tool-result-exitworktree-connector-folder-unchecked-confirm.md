<!--
name: 'Tool Result: ExitWorktree connector folder unchecked, confirm'
description: >-
  ExitWorktree validation refusal when the connector-downloads folder could not
  be checked, requiring user confirmation and discard_changes or keep
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_EXITWORKTREE_CONNECTOR_FOLDER_UNCHECKED_CONFIRM_VAR_0
  - TOOL_RESULT_EXITWORKTREE_CONNECTOR_FOLDER_UNCHECKED_CONFIRM_VAR_1
-->
Could not check the worktree's ${TOOL_RESULT_EXITWORKTREE_CONNECTOR_FOLDER_UNCHECKED_CONFIRM_VAR_0} folder, which may hold files saved from connectors that removing the worktree would delete.${TOOL_RESULT_EXITWORKTREE_CONNECTOR_FOLDER_UNCHECKED_CONFIRM_VAR_1} Refusing to remove without explicit confirmation. Confirm with the user, then re-invoke with discard_changes: true to proceed — or use action: "keep" to preserve the worktree.
