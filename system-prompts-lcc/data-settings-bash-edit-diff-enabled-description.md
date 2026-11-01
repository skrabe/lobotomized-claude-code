<!--
name: 'Data: bashEditDiffEnabled setting description'
description: >-
  Description of the `bashEditDiffEnabled` setting in Claude Code's settings
  JSON schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.316
-->
Whether the Bash tool shows a diff of the files a Bash command changed (PostToolUse Bash hooks get the changed-file list in tool_response). Set to false to turn that off. Default: off, except in auto and bypassPermissions modes when the Bash tool handles file edits or the model's configuration turns it on. Only user, flag or policy settings can turn it on in other modes.
