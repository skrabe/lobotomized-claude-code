<!--
name: 'Tool Result: Skill Deny Git Commit Disallowed Options'
description: >-
  Permission-deny suffix explaining which git commit options a skill refuses and
  to pass -m inline.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_SKILL_DENY_GIT_COMMIT_DISALLOWED_OPTIONS_VAR_0
  - TOOL_RESULT_SKILL_DENY_GIT_COMMIT_DISALLOWED_OPTIONS_VAR_1
  - TOOL_RESULT_SKILL_DENY_GIT_COMMIT_DISALLOWED_OPTIONS_VAR_2
-->
${TOOL_RESULT_SKILL_DENY_GIT_COMMIT_DISALLOWED_OPTIONS_VAR_0} refuses \`git commit\` options that read the message from a file or template, skip hooks, amend, reuse a message or allow an empty commit (tokens starting \`--fil\`, \`--te\`, \`--pathspec-fr\`, \`--no-veri\`, \`--no-g\`, \`--am\`, \`--allow-empty\`, \`--reu\`, \`--ree\`, \` -F\`, \` -t\`). The option is refused, not the commit: pass the message inline with \`-m\` as the skill's example shows. ${TOOL_RESULT_SKILL_DENY_GIT_COMMIT_DISALLOWED_OPTIONS_VAR_1} ${TOOL_RESULT_SKILL_DENY_GIT_COMMIT_DISALLOWED_OPTIONS_VAR_2}
