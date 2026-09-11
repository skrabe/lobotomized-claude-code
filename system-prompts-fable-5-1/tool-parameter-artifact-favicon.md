<!--
name: 'Tool Parameter: Artifact Favicon'
description: >-
  Zod .describe() for the Artifact tool favicon parameter (emoji on first
  publish).
ccVersion: 2.1.268
variables:
  - TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_0
  - TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_1
-->
The artifact's emoji: one or two emoji (e.g. "📊"). No markup. Required on a page's first publish; omit on a redeploy (same file path this session, or \`url\`) to keep the artifact's emoji — pass a new one only when the user asks.${TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_0?` Optional for data files on an Artifact created from an Artifact type${TOOL_PARAMETER_ARTIFACT_FAVICON_VAR_1?" and with `type_url`":""} (the type's emoji stays unless you pass one with files).`:""}
