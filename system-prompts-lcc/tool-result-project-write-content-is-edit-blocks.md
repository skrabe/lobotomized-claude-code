<!--
name: 'Tool Result: project_write content is edit blocks'
description: >-
  Refuses content that is only SEARCH/REPLACE blocks and would replace the whole
  doc
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_PROJECT_WRITE_CONTENT_IS_EDIT_BLOCKS_VAR_0
  - TOOL_RESULT_PROJECT_WRITE_CONTENT_IS_EDIT_BLOCKS_VAR_1
-->
${TOOL_RESULT_PROJECT_WRITE_CONTENT_IS_EDIT_BLOCKS_VAR_0} The text is only SEARCH/REPLACE blocks, and would have replaced the whole doc. ${TOOL_RESULT_PROJECT_WRITE_CONTENT_IS_EDIT_BLOCKS_VAR_1()?"Pass the blocks as edits, or pass":"Pass"} the doc's whole new text. Do not delete the doc to write it afresh.
