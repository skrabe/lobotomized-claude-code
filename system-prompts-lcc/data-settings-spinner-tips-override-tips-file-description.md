<!--
name: 'Data: spinnerTipsOverride.tipsFile setting description'
description: >-
  Description of the `spinnerTipsOverride.tipsFile` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Absolute or ~/ local path to a JSON file holding an array of tips (same shapes as `tips`); honored from user, --settings and on-disk managed settings only. Read once per CLI process (restart to pick up edits).
