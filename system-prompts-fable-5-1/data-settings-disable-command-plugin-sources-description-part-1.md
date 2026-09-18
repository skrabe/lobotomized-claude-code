<!--
name: 'Data: disableCommandPluginSources setting description (part 1 of 3)'
description: >-
  Description of the `disableCommandPluginSources` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Controls the `command` plugin source, whose plugin directory is produced by running a marketplace-declared command on this machine. true: command-sourced plugins are never installed, updated, or re-resolved (the command never runs). false: explicitly allowed. 
