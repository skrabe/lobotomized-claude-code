<!--
name: 'Tool Parameter: Artifact favicon'
description: >-
  Zod .describe() for the Artifact tool favicon parameter (browser-tab emoji
  icon on first publish).
ccVersion: 2.1.251
variables:
  - TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_0
  - TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_1
-->
Browser-tab icon: one or two emoji (e.g. "📊"). No markup. Required on a page's first publish; omit on a redeploy (same file path this session, or \`url\`) to keep the artifact's icon — pass a new one only when the user asks.${TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_0?` Optional for data files on an Artifact created from an Artifact type${TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_1?" and with `type_url`":""} (the type's icon stays unless you pass one with files).`:""}
