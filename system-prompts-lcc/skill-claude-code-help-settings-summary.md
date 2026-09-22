<!--
name: 'claude-code help: configured settings summary'
description: >-
  Markdown summary of configured settings keys pushed into the claude-code help
  skill's environment context injected into the model.
ccVersion: 2.1.206
variables:
  - SKILL_CLAUDE_CODE_HELP_SETTINGS_SUMMARY_VAR_0
-->
**Settings keys configured (values omitted):** ${SKILL_CLAUDE_CODE_HELP_SETTINGS_SUMMARY_VAR_0.join(", ")}. To see values, the user can run \`claude config list\` or open \`~/.claude/settings.json\`.
