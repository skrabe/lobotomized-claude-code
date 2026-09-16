<!--
name: 'Tool Description: Skill-scoped PowerShell gh pr create --base refusal'
description: >-
  Explains that an active skill refuses --base/-B on gh pr create in PowerShell
  because -b collides with --body, and to retry with --body spelled out.
ccVersion: 2.1.273
variables:
  - TOOL_DESCRIPTION_SKILL_SCOPED_GH_PR_CREATE_BASE_REFUSAL_VAR_0
  - TOOL_DESCRIPTION_SKILL_SCOPED_GH_PR_CREATE_BASE_REFUSAL_VAR_1
  - TOOL_DESCRIPTION_SKILL_SCOPED_GH_PR_CREATE_BASE_REFUSAL_VAR_2
-->
${TOOL_DESCRIPTION_SKILL_SCOPED_GH_PR_CREATE_BASE_REFUSAL_VAR_0} refuses \`--base\`/\`-B\` on \`gh pr create\` in PowerShell, where the \`-b\` short form of \`--body\` trips it too: spell it \`--body\`. The option is refused, not opening the pull request: if the default branch is the intended target, re-run it without \`--base\`, with the title and body passed inline as the skill's example shows, and the pull request opens against it. ${TOOL_DESCRIPTION_SKILL_SCOPED_GH_PR_CREATE_BASE_REFUSAL_VAR_1} ${TOOL_DESCRIPTION_SKILL_SCOPED_GH_PR_CREATE_BASE_REFUSAL_VAR_2}
