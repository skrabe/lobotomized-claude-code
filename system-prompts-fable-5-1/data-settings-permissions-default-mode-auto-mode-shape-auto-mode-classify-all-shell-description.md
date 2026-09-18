<!--
name: >-
  Data: permissions.defaultMode.autoMode.shape.autoMode.classifyAllShell setting
  description
description: >-
  Description of the
  `permissions.defaultMode.autoMode.shape.autoMode.classifyAllShell` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
When true, every Bash/PowerShell allow rule is suspended while auto mode is active so all shell commands are routed through the classifier (higher safety, more classifier calls). Default: false.
