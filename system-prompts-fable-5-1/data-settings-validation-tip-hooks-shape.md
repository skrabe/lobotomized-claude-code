<!--
name: 'Data: settings validation tip (hooks wrong shape)'
description: >-
  Suggestion appended to a settings.json validation error (hooks wrong shape);
  the model reads it in the tool result when its edit to a settings file fails
  validation.
ccVersion: 2.1.276
-->
Hooks use a matcher + hooks array. The matcher is a string: a tool name ("Bash"), pipe-separated list ("Edit|Write"), or empty to match all. Example: {"PostToolUse": [{"matcher": "Edit|Write", "hooks": [{"type": "command", "command": "echo Done"}]}]}
