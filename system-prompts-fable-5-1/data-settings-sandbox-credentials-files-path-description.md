<!--
name: 'Data: sandbox.credentials.files.path setting description'
description: >-
  Description of the `sandbox.credentials.files.path` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Path to a credential file or directory. Same resolution as sandbox.filesystem.* paths: absolute, ~ expanded, or relative to the settings file root (project root for project settings, ~/.claude for user settings).
