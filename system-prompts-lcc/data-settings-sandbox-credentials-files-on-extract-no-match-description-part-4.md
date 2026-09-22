<!--
name: >-
  Data: sandbox.credentials.files.onExtractNoMatch setting description (part 4
  of 4)
description: >-
  Description of the `sandbox.credentials.files.onExtractNoMatch` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
`sandbox.filesystem.disabled` it is treated as `error`, since read-denies are dropped in that mode; `error` aborts at sandbox setup so nothing runs until the config is fixed. Only meaningful when mode is `mask` and `extract` or `decode` is set; accepted but ignored otherwise.
