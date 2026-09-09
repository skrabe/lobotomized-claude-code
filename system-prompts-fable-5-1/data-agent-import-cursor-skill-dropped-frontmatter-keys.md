<!--
name: 'Data: Agent Import — Cursor Skill Dropped Frontmatter Keys'
description: >-
  Warning on an imported Cursor skill listing frontmatter keys Claude Code does
  not share, shown as ⚠ on the item in the /import query prompt.
ccVersion: 2.1.265
variables:
  - DATA_AGENT_IMPORT_CURSOR_SKILL_DROPPED_FRONTMATTER_KEYS_VAR_0
  - DATA_AGENT_IMPORT_CURSOR_SKILL_DROPPED_FRONTMATTER_KEYS_VAR_1
  - DATA_AGENT_IMPORT_CURSOR_SKILL_DROPPED_FRONTMATTER_KEYS_VAR_2
-->
dropped ${DATA_AGENT_IMPORT_CURSOR_SKILL_DROPPED_FRONTMATTER_KEYS_VAR_0.dropped.length} ${DATA_AGENT_IMPORT_CURSOR_SKILL_DROPPED_FRONTMATTER_KEYS_VAR_1(DATA_AGENT_IMPORT_CURSOR_SKILL_DROPPED_FRONTMATTER_KEYS_VAR_0.dropped.length,"frontmatter key")}${DATA_AGENT_IMPORT_CURSOR_SKILL_DROPPED_FRONTMATTER_KEYS_VAR_2==="user"?` (${DATA_AGENT_IMPORT_CURSOR_SKILL_DROPPED_FRONTMATTER_KEYS_VAR_0.dropped.join(", ")})`:""} that Claude Code does not share with Cursor
