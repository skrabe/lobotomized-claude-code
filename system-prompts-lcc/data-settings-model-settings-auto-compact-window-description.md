<!--
name: 'Data: modelSettings.autoCompactWindow setting description'
description: >-
  Description of the `modelSettings.autoCompactWindow` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.288
-->
Auto-compact window for this model, in tokens (100000 to 1000000), or "auto" for the window tuned for the model. Within one settings file it replaces the top-level autoCompactWindow for the model. /autocompact saves here. The canonical model name as key also matches its dated, [1m], Bedrock and Vertex spellings.
