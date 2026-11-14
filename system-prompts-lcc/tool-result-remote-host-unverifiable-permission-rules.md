<!--
name: 'Tool Result: remote host unverifiable permission rules'
description: >-
  Refusal when file/command permission rules cannot be checked on another
  machine's disk or shell
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_HOST_UNVERIFIABLE_PERMISSION_RULES_VAR_0
  - TOOL_RESULT_REMOTE_HOST_UNVERIFIABLE_PERMISSION_RULES_VAR_1
-->
This session holds permission rules on files or commands that it can't check here, because it can't see ${TOOL_RESULT_REMOTE_HOST_UNVERIFIABLE_PERMISSION_RULES_VAR_0.name}'s disk or shell. So it sends no ${TOOL_RESULT_REMOTE_HOST_UNVERIFIABLE_PERMISSION_RULES_VAR_1.name} call there while they stand, and retrying or respelling the call won't help. Tell the person: whoever set the rules, often their organization's administrator, can change them, unless they are built into this build. ${TOOL_RESULT_REMOTE_HOST_UNVERIFIABLE_PERMISSION_RULES_VAR_0.name}'s MCP tools aren't stopped by this.
