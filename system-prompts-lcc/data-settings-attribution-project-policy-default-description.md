<!--
name: 'Data: attributionProjectPolicy.default setting description'
description: >-
  Description of the `attributionProjectPolicy.default` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.328
-->
The Project used when neither CLAUDE_CODE_ATTRIBUTION_PROJECT nor attributionProject names one: its ID, starting with "claude_proj_" or "chan_", or the UUID of a "claude_proj_" Project. Behind a Claude apps gateway that reports usage by group, a group name instead.
