<!--
name: 'Data: sandbox.filesystem.disabled setting description (part 5 of 7)'
description: >-
  Description of the `sandbox.filesystem.disabled` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
project settings (.claude/settings.json and .claude/settings.local.json) are ignored. If managed settings configure sandbox.filesystem at all, or list any sandbox.credentials.files deny entry, only managed settings can set this: an admin who deployed filesystem restrictions must not have them switched off by a user-writable file. (sandbox.credentials.envVars and credentials.files mask entries 
