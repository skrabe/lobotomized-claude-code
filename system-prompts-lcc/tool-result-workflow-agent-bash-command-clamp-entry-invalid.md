<!--
name: 'Tool Result: workflow agent() bashCommandClamp entry invalid'
description: >-
  Error thrown into a workflow script when a bashCommandClamp entry is not a
  well-formed Bash(<command or prefix>) permission rule.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKFLOW_AGENT_BASH_COMMAND_CLAMP_ENTRY_INVALID_VAR_0
  - TOOL_RESULT_WORKFLOW_AGENT_BASH_COMMAND_CLAMP_ENTRY_INVALID_VAR_1
  - TOOL_RESULT_WORKFLOW_AGENT_BASH_COMMAND_CLAMP_ENTRY_INVALID_VAR_2
-->
agent() opts.bashCommandClamp entry '${TOOL_RESULT_WORKFLOW_AGENT_BASH_COMMAND_CLAMP_ENTRY_INVALID_VAR_0}' must be a '${TOOL_RESULT_WORKFLOW_AGENT_BASH_COMMAND_CLAMP_ENTRY_INVALID_VAR_1}(<command or prefix>)' permission rule (tool name case-sensitive, non-empty content with no leading/trailing whitespace inside the parens); it parses to tool '${TOOL_RESULT_WORKFLOW_AGENT_BASH_COMMAND_CLAMP_ENTRY_INVALID_VAR_2}'
