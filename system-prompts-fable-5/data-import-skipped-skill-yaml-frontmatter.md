<!--
name: 'Data: Codex skill import skipped for YAML frontmatter'
description: >-
  Skip reason recorded when /import declines to copy a Codex skill whose
  SKILL.md begins with YAML frontmatter; surfaces to the model through the local
  /import command's <local-command-stdout>.
ccVersion: 2.1.224
variables:
  - DATA_IMPORT_SKIPPED_SKILL_YAML_FRONTMATTER_VAR_0
-->
${DATA_IMPORT_SKIPPED_SKILL_YAML_FRONTMATTER_VAR_0}: SKILL.md starts with \`---\` — Codex treats SKILL.md as plain text, so any YAML frontmatter is Claude-Code-only and would take effect on import. Copy the skill manually after reviewing what each key enables.
