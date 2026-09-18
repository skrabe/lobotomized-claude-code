<!--
name: 'Data: sandbox.credentials.files.decode setting description'
description: >-
  Description of the `sandbox.credentials.files.decode` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Optional encoded-credential format for `mask` mode. `jwt`: candidates are located with a built-in JWT regex (or the explicit `extract` pattern, if set), verified to actually be JWTs before masking, and replaced with a structurally valid fake JWT so client-side token parsing inside the sandbox keeps working. If no candidate verifies, behavior is governed by `onExtractNoMatch` (default `warn`). Accepted but ignored for `deny`.
