<!--
name: 'Data: sandbox.autoAllowBashIfSandboxed setting description'
description: >-
  Description of the `sandbox.autoAllowBashIfSandboxed` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.325
-->
macOS and Linux/WSL only: approve a Bash command that will run inside the sandbox without a permission prompt, unless a deny rule, a command-specific ask rule or a safety check stops it. Default: false, so sandboxed commands go through the same permission flow as any other command. Has no effect on native Windows.
