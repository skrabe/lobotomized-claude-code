<!--
name: 'Tool Parameter: Artifact favicon'
description: Artifact tool favicon parameter — one or two emoji for the browser-tab icon
ccVersion: 2.1.237
variables:
  - TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_0
  - TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_1
-->
Browser-tab icon: one or two emoji (e.g. "📊"). No markup. Required to publish${TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_0?` a page; optional for data files on an Artifact created from an Artifact type${TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_1?" and with `type_url`":""} (the type's icon stays unless you pass one with files)`:""}. Keep stable across redeploys; change only on a hard topic pivot.
