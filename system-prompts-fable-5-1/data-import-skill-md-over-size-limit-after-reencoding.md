<!--
name: 'Data: Import Skill Over Size Limit After Re-encoding'
description: >-
  Skip reason reported in /import output when a Codex skill's SKILL.md would
  exceed the loadable byte limit once re-encoded as UTF-8.
ccVersion: 2.1.224
variables:
  - DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_AFTER_REENCODING_VAR_0
  - DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_AFTER_REENCODING_VAR_1
  - DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_AFTER_REENCODING_VAR_2
-->
${DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_AFTER_REENCODING_VAR_0}: SKILL.md would be ${DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_AFTER_REENCODING_VAR_1} bytes after utf-8 re-encoding — Claude Code skips skills over ${DATA_IMPORT_SKILL_MD_OVER_SIZE_LIMIT_AFTER_REENCODING_VAR_2} bytes
