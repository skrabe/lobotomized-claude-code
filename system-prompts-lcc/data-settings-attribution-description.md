<!--
name: 'Data: attribution setting description'
description: >-
  Description of the `attribution` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.281
-->
Customize attribution text for commits and PRs. Each field defaults to the standard Claude Code attribution if not set. Set to false to hide all attribution, the same as { "commit": "", "pr": "", "sessionUrl": false }. Setting it to true is the same as leaving it out. Older Claude Code versions reject true or false here, so use the object form in settings files shared across versions.
