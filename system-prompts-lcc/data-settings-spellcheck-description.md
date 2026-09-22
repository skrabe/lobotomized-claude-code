<!--
name: 'Data: spellcheck setting description'
description: >-
  Description of the `spellcheck` setting in Claude Code's settings JSON schema.
  The model reads it through /update-config and settings validation errors; it
  is also shown to users in the settings help.
ccVersion: 2.1.276
variables:
  - DATA_SETTINGS_SPELLCHECK_DESCRIPTION_VAR_0
-->
Underline misspelled words in the prompt input as you type, using an installed ${DATA_SETTINGS_SPELLCHECK_DESCRIPTION_VAR_0.slice(0,-1).join(", ")} or ${DATA_SETTINGS_SPELLCHECK_DESCRIPTION_VAR_0.at(-1)} (off unless "enabled" is true; does nothing if none is installed). Read from user, flag and managed settings only (the whole block from the highest-precedence of those applies); ignored in project .claude/settings.json and .claude/settings.local.json.
