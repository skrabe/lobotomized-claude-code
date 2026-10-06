<!--
name: 'Skill: Claude API Managed Agents quickstarts list'
description: >-
  Bundled quickstarts section header of the Claude API skill listing the
  quickstart templates and their files.
ccVersion: 2.1.291
variables:
  - SKILL_CLAUDE_API_MANAGED_AGENTS_QUICKSTARTS_LIST_VAR_0
  - SKILL_CLAUDE_API_MANAGED_AGENTS_QUICKSTARTS_LIST_VAR_1
  - SKILL_CLAUDE_API_MANAGED_AGENTS_QUICKSTARTS_LIST_VAR_2
-->
## Bundled Quickstarts

\`/claude-api managed-agents-onboard <name>\` builds one of these, the templates on the Console's quickstart page. One file each under \`${SKILL_CLAUDE_API_MANAGED_AGENTS_QUICKSTARTS_LIST_VAR_0}\`:

${SKILL_CLAUDE_API_MANAGED_AGENTS_QUICKSTARTS_LIST_VAR_1.map((SKILL_CLAUDE_API_MANAGED_AGENTS_QUICKSTARTS_LIST_VAR_2)=>`- \`${SKILL_CLAUDE_API_MANAGED_AGENTS_QUICKSTARTS_LIST_VAR_2.name}\` - ${SKILL_CLAUDE_API_MANAGED_AGENTS_QUICKSTARTS_LIST_VAR_2.description}`).join(`
`)}
