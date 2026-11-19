<!--
name: 'Tool Result: project_write edits doc not in view'
description: >-
  Edit refusal when the doc's whole current text is not in context, asking to
  project_read first
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_PROJECT_WRITE_EDITS_DOC_NOT_IN_VIEW_VAR_0
-->
${TOOL_RESULT_PROJECT_WRITE_EDITS_DOC_NOT_IN_VIEW_VAR_0} This tool cannot find the doc's whole current text in your context. Call project_read on this path. If it shows the whole text, send the blocks again against that text. If it does not, follow what its result tells you: edits cannot be used for this doc.
