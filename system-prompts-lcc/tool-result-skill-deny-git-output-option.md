<!--
name: 'Tool Result: Skill Deny Git Output Option'
description: >-
  Permission-deny suffix refusing git --output because it writes to an arbitrary
  path.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_SKILL_DENY_GIT_OUTPUT_OPTION_VAR_0
  - TOOL_RESULT_SKILL_DENY_GIT_OUTPUT_OPTION_VAR_1
-->
${TOOL_RESULT_SKILL_DENY_GIT_OUTPUT_OPTION_VAR_0} refuses \`--output\` on git commands (it writes to an arbitrary path): drop it and read stdout. ${TOOL_RESULT_SKILL_DENY_GIT_OUTPUT_OPTION_VAR_1}
