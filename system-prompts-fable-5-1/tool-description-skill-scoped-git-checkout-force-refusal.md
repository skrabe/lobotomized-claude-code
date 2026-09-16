<!--
name: 'Tool Description: Skill-scoped git checkout --force refusal'
description: >-
  Explains that an active skill refuses git checkout --force/-f and to create
  the branch with a plain git checkout -b.
ccVersion: 2.1.273
variables:
  - TOOL_DESCRIPTION_SKILL_SCOPED_GIT_CHECKOUT_FORCE_REFUSAL_VAR_0
  - TOOL_DESCRIPTION_SKILL_SCOPED_GIT_CHECKOUT_FORCE_REFUSAL_VAR_1
-->
${TOOL_DESCRIPTION_SKILL_SCOPED_GIT_CHECKOUT_FORCE_REFUSAL_VAR_0} refuses \`git checkout\` with \`--force\`/\`-f\` (tokens starting \`--f\` or \` -f\`): create the branch with a plain \`git checkout -b\`. The match is on the raw command text, so a branch name containing \`--f\` trips it too. ${TOOL_DESCRIPTION_SKILL_SCOPED_GIT_CHECKOUT_FORCE_REFUSAL_VAR_1}
