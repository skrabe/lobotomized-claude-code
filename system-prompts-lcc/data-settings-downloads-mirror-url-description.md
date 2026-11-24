<!--
name: 'Data: downloadsMirrorUrl setting description'
description: >-
  Description of the `downloadsMirrorUrl` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.331
-->
Anthropic-run mirror from which native installs download Claude Code releases (claude install, claude update, and auto-updates), instead of https://downloads.claude.ai. Must be exactly https://claude.fedstart.com/claude-downloads (Claude for Government). Any other value stops installs and updates with an error. CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC normally turns auto-updates off, but not with this mirror set. Only read from managed (policy) settings.
