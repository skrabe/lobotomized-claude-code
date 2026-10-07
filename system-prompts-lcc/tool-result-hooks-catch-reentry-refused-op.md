<!--
name: 'Tool Result: Hooks .catch re-entry refused host op'
description: >-
  Refusal when a hooks-module .catch asked for re-entry and then tries a host op
  other than calling its own next()
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_HOOKS_CATCH_REENTRY_REFUSED_OP_VAR_0
  - TOOL_RESULT_HOOKS_CATCH_REENTRY_REFUSED_OP_VAR_1
  - TOOL_RESULT_HOOKS_CATCH_REENTRY_REFUSED_OP_VAR_2
  - TOOL_RESULT_HOOKS_CATCH_REENTRY_REFUSED_OP_VAR_3
-->
${TOOL_RESULT_HOOKS_CATCH_REENTRY_REFUSED_OP_VAR_0.environments.get(TOOL_RESULT_HOOKS_CATCH_REENTRY_REFUSED_OP_VAR_1)?.TOOL_RESULT_HOOKS_CATCH_REENTRY_REFUSED_OP_VAR_2}: ${TOOL_RESULT_HOOKS_CATCH_REENTRY_REFUSED_OP_VAR_3} refused: a .catch asked because re-entry left its hook out answers and calls its own next(), nothing else
