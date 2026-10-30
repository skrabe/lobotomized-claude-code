<!--
name: 'Tool Result: Auto mode no result, deny rules hold'
description: >-
  Deny tool_result when auto mode's safety check gave no result (or does not run
  this session) and nobody is asked because the settings hold auto mode deny
  rules.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_AUTO_MODE_NO_RESULT_DENY_RULES_HOLD_VAR_0
  - TOOL_RESULT_AUTO_MODE_NO_RESULT_DENY_RULES_HOLD_VAR_1
  - TOOL_RESULT_AUTO_MODE_NO_RESULT_DENY_RULES_HOLD_VAR_2
-->
${TOOL_RESULT_AUTO_MODE_NO_RESULT_DENY_RULES_HOLD_VAR_0.name} was not run: auto mode's safety check ${TOOL_RESULT_AUTO_MODE_NO_RESULT_DENY_RULES_HOLD_VAR_1===void 0?"does not run for this session":"gave no result"}, and nobody is asked to approve it in its place, because the settings hold auto mode deny rules, which only the automatic check applies. This is not a judgment that the action is unsafe. ${TOOL_RESULT_AUTO_MODE_NO_RESULT_DENY_RULES_HOLD_VAR_1===void 0?"Other actions that need the check will be denied too, and retrying won't help. Finish what you can without them, then tell the user what is blocked and why.":`${TOOL_RESULT_AUTO_MODE_NO_RESULT_DENY_RULES_HOLD_VAR_2} then tell the user that it was not run and why.`}
