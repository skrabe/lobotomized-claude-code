<!--
name: 'Tool Result: Steward push ambiguous ref'
description: Refuses a push when a similarly spelled ref could be pushed instead
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_PUSH_AMBIGUOUS_REF_VAR_0
  - TOOL_RESULT_STEWARD_PUSH_AMBIGUOUS_REF_VAR_1
  - TOOL_RESULT_STEWARD_PUSH_AMBIGUOUS_REF_VAR_2
-->
this checkout holds a ref spelled like ${TOOL_RESULT_STEWARD_PUSH_AMBIGUOUS_REF_VAR_0(TOOL_RESULT_STEWARD_PUSH_AMBIGUOUS_REF_VAR_1[0])}, which git push could take for ${TOOL_RESULT_STEWARD_PUSH_AMBIGUOUS_REF_VAR_2} in place of the commit that is checked here. Push nothing, and tell the user
