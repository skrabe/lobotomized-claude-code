<!--
name: 'Data: sandbox.allowUnsandboxedCommands setting description'
description: >-
  Description of the `sandbox.allowUnsandboxedCommands` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Allow commands to run outside the sandbox via the dangerouslyDisableSandbox parameter. When false, the dangerouslyDisableSandbox parameter is completely ignored and all commands must run sandboxed. Default: true.
