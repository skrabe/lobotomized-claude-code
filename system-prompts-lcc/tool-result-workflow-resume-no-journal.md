<!--
name: 'Tool Result: Workflow Resume No Journal'
description: >-
  Workflow-tool refusal when resumeFromRunId has no journal entries, telling the
  model to call Workflow again without that id.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_WORKFLOW_RESUME_NO_JOURNAL_VAR_0
-->
No journal found for workflow run ${TOOL_RESULT_WORKFLOW_RESUME_NO_JOURNAL_VAR_0}, so there is nothing to resume. To run the workflow from the start, call Workflow again without resumeFromRunId.
