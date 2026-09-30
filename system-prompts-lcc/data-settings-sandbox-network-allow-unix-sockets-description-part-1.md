<!--
name: 'Data: sandbox.network.allowUnixSockets setting description (part 1 of 2)'
description: >-
  Description of the `sandbox.network.allowUnixSockets` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.285
-->
macOS only: Unix socket paths to allow. Ignored on Linux (seccomp cannot filter by path). Merged across settings sources. 
