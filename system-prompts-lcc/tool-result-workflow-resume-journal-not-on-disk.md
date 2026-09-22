<!--
name: Workflow Resume Journal Not On Disk
description: >-
  Workflow tool_result when resume cannot find a local journal and this session
  cannot fetch a remote copy, with a fallback to hand-author from agent jsonl
  files.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_WORKFLOW_RESUME_JOURNAL_NOT_ON_DISK_VAR_0
  - TOOL_RESULT_WORKFLOW_RESUME_JOURNAL_NOT_ON_DISK_VAR_1
-->
The journal for workflow run ${TOOL_RESULT_WORKFLOW_RESUME_JOURNAL_NOT_ON_DISK_VAR_0} is not on disk, and this session cannot fetch a remote copy, so there is nothing to resume. Fallback: Read the agent-<id>.jsonl files in ${TOOL_RESULT_WORKFLOW_RESUME_JOURNAL_NOT_ON_DISK_VAR_1(TOOL_RESULT_WORKFLOW_RESUME_JOURNAL_NOT_ON_DISK_VAR_0)} and hand-author a continuation script.
