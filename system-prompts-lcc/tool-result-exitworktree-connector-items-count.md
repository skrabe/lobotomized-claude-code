<!--
name: 'Tool Result: ExitWorktree connector items count'
description: >-
  List item for ExitWorktree's at-risk work counting items saved from connectors
  in a folder git does not track
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_EXITWORKTREE_CONNECTOR_ITEMS_COUNT_VAR_0
  - TOOL_RESULT_EXITWORKTREE_CONNECTOR_ITEMS_COUNT_VAR_1
-->
${TOOL_RESULT_EXITWORKTREE_CONNECTOR_ITEMS_COUNT_VAR_0===1?"1 item":`${TOOL_RESULT_EXITWORKTREE_CONNECTOR_ITEMS_COUNT_VAR_0} items`} saved from connectors in ${TOOL_RESULT_EXITWORKTREE_CONNECTOR_ITEMS_COUNT_VAR_1}, a folder git doesn't track
