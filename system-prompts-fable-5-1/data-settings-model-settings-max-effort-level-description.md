<!--
name: 'Data: modelSettings.maxEffortLevel setting description'
description: >-
  Description of the `modelSettings.maxEffortLevel` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Maximum effort level for this model. Within one settings file it replaces the top-level maxEffortLevel for the model ("max" exempts it); across settings files the lowest applicable value wins. Keyed like effortLevel: the canonical model name also matches its dated, [1m], Bedrock and Vertex spellings.
