<!--
name: >-
  Data: sandbox.credentials.files.onExtractNoMatch setting description (part 2
  of 4)
description: >-
  Description of the `sandbox.credentials.files.onExtractNoMatch` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
with `decode`, when no candidate survives verification. `warn` (default) emits a stderr warning and leaves the file readable as-is inside the sandbox (fail-open, for credentials that may be legitimately absent); `deny` degrades the entry to 
