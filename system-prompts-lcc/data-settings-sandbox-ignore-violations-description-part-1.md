<!--
name: 'Data: sandbox.ignoreViolations setting description (part 1 of 2)'
description: >-
  Description of the `sandbox.ignoreViolations` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.285
-->
Sandbox violations to leave unreported: a map of command patterns ("*" for every command) to the filesystem paths whose violations are ignored. Merged across settings sources. 
