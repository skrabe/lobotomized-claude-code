<!--
name: 'Tool result: Artifact list type ask rule added after check'
description: Artifact list error when an ask rule was added after the permission check ran.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_ADDED_AFTER_CHECK_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_ADDED_AFTER_CHECK_VAR_1
-->
The permission rule ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_ADDED_AFTER_CHECK_VAR_0(TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_ADDED_AFTER_CHECK_VAR_1)} asks the user before this type is listed, and it was added after this call's permission check ran, so nothing was listed. List it again the same way to have the user asked.
