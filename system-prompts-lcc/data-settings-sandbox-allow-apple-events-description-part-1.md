<!--
name: 'Data: sandbox.allowAppleEvents setting description (part 1 of 5)'
description: >-
  Description of the `sandbox.allowAppleEvents` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
macOS only: Allow sandboxed commands to send Apple Events (and look up the appleeventsd Mach service). Needed for `open`, `osascript`, and browser-based auth flows that open URLs. 
