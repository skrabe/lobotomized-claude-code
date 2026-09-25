<!--
name: 'Tool Result: Skill Permission — Non-Holder Needs Approval Each Time'
description: >-
  ue() nonholder case: the rule cannot pre-approve this skill because it comes
  from a plugin or is not synced, so it needs approval each time.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_SKILL_PERMISSION_RULE_NONHOLDER_NEEDS_APPROVAL_VAR_0
  - TOOL_RESULT_SKILL_PERMISSION_RULE_NONHOLDER_NEEDS_APPROVAL_VAR_1
  - TOOL_RESULT_SKILL_PERMISSION_RULE_NONHOLDER_NEEDS_APPROVAL_VAR_2
-->
${TOOL_RESULT_SKILL_PERMISSION_RULE_NONHOLDER_NEEDS_APPROVAL_VAR_0} ${TOOL_RESULT_SKILL_PERMISSION_RULE_NONHOLDER_NEEDS_APPROVAL_VAR_1} ${TOOL_RESULT_SKILL_PERMISSION_RULE_NONHOLDER_NEEDS_APPROVAL_VAR_2.pluginName!==void 0?`comes from the plugin "${TOOL_RESULT_SKILL_PERMISSION_RULE_NONHOLDER_NEEDS_APPROVAL_VAR_2.pluginName}"`:"is not synced"}, so no rule for that name can pre-approve it; it needs approval each time.
