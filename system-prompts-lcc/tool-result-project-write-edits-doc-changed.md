<!--
name: 'Tool Result: project_write edits doc changed'
description: >-
  Edit refusal when the doc changed since last read, asking to re-read and send
  only missing blocks
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_PROJECT_WRITE_EDITS_DOC_CHANGED_VAR_0
-->
${TOOL_RESULT_PROJECT_WRITE_EDITS_DOC_CHANGED_VAR_0} The doc at this path has changed since you last read or wrote it in this conversation. Call project_read on this path and check whether your change is already in it: an earlier try may have been saved. Then send blocks only for what is still missing.
