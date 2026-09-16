<!--
name: 'Tool Result: Skill Deny Git Add Force Chmod'
description: >-
  Permission-deny suffix refusing git add --force/--chmod so ignored files are
  not staged.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_SKILL_DENY_GIT_ADD_FORCE_CHMOD_VAR_0
  - TOOL_RESULT_SKILL_DENY_GIT_ADD_FORCE_CHMOD_VAR_1
  - TOOL_RESULT_SKILL_DENY_GIT_ADD_FORCE_CHMOD_VAR_2
-->
${TOOL_RESULT_SKILL_DENY_GIT_ADD_FORCE_CHMOD_VAR_0} refuses \`git add\` with \`--force\`/\`-f\` (it stages ignored files such as \`.env\`) or \`--chmod\` (tokens starting \`--f\`, \`-f\`, \`--c\`): stage the paths by name without the option. ${TOOL_RESULT_SKILL_DENY_GIT_ADD_FORCE_CHMOD_VAR_1} ${TOOL_RESULT_SKILL_DENY_GIT_ADD_FORCE_CHMOD_VAR_2}
