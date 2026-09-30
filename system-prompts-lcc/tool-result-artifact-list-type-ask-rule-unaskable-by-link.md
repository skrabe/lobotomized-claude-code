<!--
name: 'Tool Result: Artifact list type ask rule cannot ask when listed by link'
description: >-
  Error returned when a permission ask rule covers a type that can be listed
  only by its link, where nothing can ask the user, telling the model to tell
  the user and suggest a type_url ask rule
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_UNASKABLE_BY_LINK_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_UNASKABLE_BY_LINK_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_UNASKABLE_BY_LINK_VAR_2
-->
The permission rule ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_UNASKABLE_BY_LINK_VAR_0(TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_UNASKABLE_BY_LINK_VAR_1)} asks the user before the ${TOOL_RESULT_ARTIFACT_LIST_TYPE_ASK_RULE_UNASKABLE_BY_LINK_VAR_2} type is listed, and this type can be listed only by its link, where nothing can ask the user, so nothing was listed. Tell the user; an ask rule naming the link (\`type_url:\`) would let them be asked.
