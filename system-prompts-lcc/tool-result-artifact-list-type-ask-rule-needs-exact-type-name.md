<!--
name: 'Tool Result: Artifact list ask rule needs exact type name'
description: >-
  Error from the artifact tool's list-by-type action when a permission ask rule
  covers the type but only asks when `type` matches the rule exactly, so nothing
  was listed and the model should list again with the exact type name.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_2
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_3
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_4
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_5
-->
The permission rule ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_0(TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_1)} asks the user before the ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_2} type is listed, and the user is asked only when \`type\` matches the rule, so nothing was listed. To have the user asked, list it again with \`type\` set to exactly ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_3(TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_4(TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_NEEDS_EXACT_TYPE_NAME_VAR_5))}.
