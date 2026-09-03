<!--
name: 'Data: Import Skill SKILL.md Over Size Limit'
description: >-
  Skip reason reported in /import output when a Codex skill's SKILL.md is larger
  than the byte limit Claude Code will load.
ccVersion: 2.1.224
variables:
  - DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_VAR_0
  - DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_VAR_1
  - DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_VAR_2
-->
${DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_VAR_0}: SKILL.md is ${DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_VAR_1.size} bytes — Claude Code skips skills over ${DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_VAR_2} bytes, so the copy would never load
