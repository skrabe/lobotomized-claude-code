<!--
name: 'Data: spellcheck.checker setting description'
description: >-
  Description of the `spellcheck.checker` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
variables:
  - DATA_SETTINGS_SPELLCHECK_CHECKER_DESCRIPTION_VAR_0
  - DATA_SETTINGS_SPELLCHECK_CHECKER_DESCRIPTION_VAR_1
-->
Which spell checker to run: ${DATA_SETTINGS_SPELLCHECK_CHECKER_DESCRIPTION_VAR_0.map((DATA_SETTINGS_SPELLCHECK_CHECKER_DESCRIPTION_VAR_1)=>`"${DATA_SETTINGS_SPELLCHECK_CHECKER_DESCRIPTION_VAR_1}"`).join(", ")}, or "auto" (default) for the first of those found on PATH
