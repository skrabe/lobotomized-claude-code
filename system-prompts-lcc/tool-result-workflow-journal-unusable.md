<!--
name: 'Tool Result: Workflow journal unusable'
description: >-
  Workflow failure when the journal file can't be used (link or second hard
  link); delete it and start the run again.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_WORKFLOW_JOURNAL_UNUSABLE_VAR_0
  - TOOL_RESULT_WORKFLOW_JOURNAL_UNUSABLE_VAR_1
-->
could not use the workflow journal ${this.path} (${TOOL_RESULT_WORKFLOW_JOURNAL_UNUSABLE_VAR_0(TOOL_RESULT_WORKFLOW_JOURNAL_UNUSABLE_VAR_1)}). If that file is a link, delete it. If it has a second hard link, delete the other name. Then start the run again.
