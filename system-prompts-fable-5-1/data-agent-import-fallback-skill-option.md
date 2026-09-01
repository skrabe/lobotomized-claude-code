<!--
name: 'Data: Agent Import — Fallback Skill Option'
description: >-
  Prompt bullet in the `/import` query prompt explaining that `--yes` also
  writes the import-to-claude-code reference skill for unmapped items.
ccVersion: 2.1.214
variables:
  - DATA_AGENT_IMPORT_FALLBACK_SKILL_OPTION_VAR_0
-->
- \`${DATA_AGENT_IMPORT_FALLBACK_SKILL_OPTION_VAR_0}\` also writes a reference skill (\`skills/import-to-claude-code/\` in the Claude config directory) capturing the unmapped items above for manual porting — to skip that write, use the terminal picker instead.
