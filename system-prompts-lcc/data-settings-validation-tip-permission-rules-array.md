<!--
name: 'Data: settings validation tip (permission rules not an array)'
description: >-
  Suggestion appended to a settings.json validation error (permission rules not
  an array); the model reads it in the tool result when its edit to a settings
  file fails validation.
ccVersion: 2.1.276
-->
Permission rules must be in an array. Format: ["Tool(specifier)"]. Examples: ["Bash(npm run build)", "Edit(docs/**)", "Read(~/.zshrc)"]. Use * for wildcards.
