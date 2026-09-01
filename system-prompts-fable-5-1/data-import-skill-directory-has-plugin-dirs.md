<!--
name: 'Data: Import Skill Directory Has Plugin Dirs'
description: >-
  Skip reason reported in /import output when a Codex skill directory contains
  subdirectories Claude Code would adopt as plugin surfaces.
ccVersion: 2.1.224
variables:
  - DATA_IMPORT_SKILL_DIRECTORY_HAS_PLUGIN_DIRS_VAR_0
  - DATA_IMPORT_SKILL_DIRECTORY_HAS_PLUGIN_DIRS_VAR_1
  - DATA_IMPORT_SKILL_DIRECTORY_HAS_PLUGIN_DIRS_VAR_2
-->
${DATA_IMPORT_SKILL_DIRECTORY_HAS_PLUGIN_DIRS_VAR_0}: skill directory contains ${DATA_IMPORT_SKILL_DIRECTORY_HAS_PLUGIN_DIRS_VAR_1.map((DATA_IMPORT_SKILL_DIRECTORY_HAS_PLUGIN_DIRS_VAR_2)=>`\`${DATA_IMPORT_SKILL_DIRECTORY_HAS_PLUGIN_DIRS_VAR_2}/\``).join(", ")} which Claude Code would adopt as a plugin (lifecycle hooks, monitors, MCP servers) — copy it manually after reviewing those
