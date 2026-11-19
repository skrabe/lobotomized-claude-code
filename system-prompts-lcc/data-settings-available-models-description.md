<!--
name: 'Data: availableModels setting description'
description: >-
  Description of the `availableModels` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.328
-->
Allowlist of models that users can select. Accepts family aliases ("opus" allows any opus version), version prefixes ("opus-4-5" allows that version and any model ID that extends it, so "claude-opus-5" also allows "claude-opus-5-5"), and full model IDs. An entry with a path before the model ID (a gateway route such as "route/claude-opus-5") does not allow the plain ID ("claude-opus-5"): list the plain ID too if some sessions send requests directly to the Anthropic API. If undefined, all models are available. If empty array, only the default model is available. Typically set in managed settings by enterprise administrators.
