<!--
name: 'Claude Code Skill: Available Commands Inventory Header'
description: >-
  Header line of the built-in-command inventory that lWT assembles into the
  claude-code help skill's context so the model knows which slash commands exist
  in the running build.
ccVersion: 2.1.221
variables:
  - SKILL_CLAUDE_CODE_HELP_AVAILABLE_COMMANDS_VAR_0
  - SKILL_CLAUDE_CODE_HELP_AVAILABLE_COMMANDS_VAR_1
-->

**Available commands (${SKILL_CLAUDE_CODE_HELP_AVAILABLE_COMMANDS_VAR_0.length} in this build):**
${SKILL_CLAUDE_CODE_HELP_AVAILABLE_COMMANDS_VAR_1.join(`
`)}
