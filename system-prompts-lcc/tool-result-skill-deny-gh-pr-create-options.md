<!--
name: 'Tool Result: Skill Deny Gh Pr Create Options'
description: >-
  Permission-deny suffix for refused gh pr create flags, telling the model to
  retry with inline title and body.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_SKILL_DENY_GH_PR_CREATE_OPTIONS_VAR_0
  - TOOL_RESULT_SKILL_DENY_GH_PR_CREATE_OPTIONS_VAR_1
  - TOOL_RESULT_SKILL_DENY_GH_PR_CREATE_OPTIONS_VAR_2
-->
${TOOL_RESULT_SKILL_DENY_GH_PR_CREATE_OPTIONS_VAR_0} runs \`gh pr create\` only in its instructed form and refuses \`--repo\`/\`-R\`, \`--head\`/\`-H\`, \`--body-file\`/\`-F\` and \`--recover\` on it. The option is refused, not opening the pull request: re-run it with the title and body passed inline as the skill's example shows; that retry is the intended fix, not a workaround. ${TOOL_RESULT_SKILL_DENY_GH_PR_CREATE_OPTIONS_VAR_1} ${TOOL_RESULT_SKILL_DENY_GH_PR_CREATE_OPTIONS_VAR_2}
