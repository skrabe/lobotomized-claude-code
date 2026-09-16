<!--
name: 'Tool Result: Workflow Usage Limit Already Waited'
description: >-
  Workflow wait decline note when this run already waited for the configured
  number of usage-limit resets, delivered in the same <failures>/remote-workflow
  payload as its sibling.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_0
  - TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_1
  - TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_2
  - TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_3
  - TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_4
-->
usage limit; resets ${TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_0(TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_1.resetsAt)}, and this run already waited for ${TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_2?TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_3:TOOL_RESULT_WORKFLOW_USAGE_LIMIT_ALREADY_WAITED_VAR_4} resets
