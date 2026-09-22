<!--
name: 'Data: sandbox.credentials.files.mode setting description (part 1 of 3)'
description: >-
  Description of the `sandbox.credentials.files.mode` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Access mode for this path. `deny` blocks reads inside the sandbox; `mask` shows sandboxed commands a sentinel-substituted copy (whole-file, or only the spans captured by `extract`) and the 
