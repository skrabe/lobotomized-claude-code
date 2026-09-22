<!--
name: 'Tool result: Artifact publish root read blocked by deny rule'
description: >-
  Hard-deny message when the Artifact publish `root` base directory is blocked
  by a Read deny rule, returned to the model as the block reason.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_READ_BLOCKED_DENY_RULE_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_READ_BLOCKED_DENY_RULE_VAR_1
-->
root: reading from under ${TOOL_RESULT_ARTIFACT_ROOT_READ_BLOCKED_DENY_RULE_VAR_0(TOOL_RESULT_ARTIFACT_ROOT_READ_BLOCKED_DENY_RULE_VAR_1)} is blocked by a Read permission rule
