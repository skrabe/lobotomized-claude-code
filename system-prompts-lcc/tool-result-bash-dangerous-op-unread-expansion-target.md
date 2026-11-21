<!--
name: 'Tool Result: dangerous op target with unreadable expansion'
description: >-
  Ask message when a removal target holds a shell expansion the check cannot
  work out
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_1
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_2
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_3
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_4
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_0} operation detected in \`${TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_1}\`${TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_2}. The target '${TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_3}' holds a shell expansion whose value this check can't work out. When $${TOOL_RESULT_BASH_DANGEROUS_OP_UNREAD_EXPANSION_TARGET_VAR_4.unreadExpansionOf} is unset or empty, it may become \`/\`, \`/*\`, or a top-level path. This requires explicit approval and cannot be auto-allowed by permission rules.
