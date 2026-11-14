<!--
name: 'Data: sandbox.failIfUnavailable setting description'
description: >-
  Description of the `sandbox.failIfUnavailable` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.325
-->
Exit with an error at startup if sandbox.enabled is true but the sandbox cannot start (missing dependencies or unsupported platform). When false (default), a warning is shown and commands run unsandboxed. Intended for managed-settings deployments that require sandboxing as a hard gate. A Claude Code on the web, scheduled-task or Cowork cloud session (Anthropic's cloud container, which has no command sandbox) starts anyway with a warning: the container isolates it, and the sandbox.filesystem and sandbox.network rules in settings are not enforced there. 
