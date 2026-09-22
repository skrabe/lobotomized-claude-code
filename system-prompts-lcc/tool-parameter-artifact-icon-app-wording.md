<!--
name: 'Tool Parameter: Artifact Icon App Wording'
description: >-
  App-worded Artifact icon parameter description: Claude includes the word on
  first publish and omits it on a redeploy.
ccVersion: 2.1.276
variables:
  - TOOL_PARAMETER_ARTIFACT_ICON_APP_WORDING_VAR_0
-->
One short generic word for the artifact's browser-tab icon, such as chart, calendar, recipe, code or map: a plain signifier, never a product or brand name. Claude includes it on every page's first publish and omits it on a redeploy so the artifact keeps its icon, passing a new one only when the person asks.${TOOL_PARAMETER_ARTIFACT_ICON_APP_WORDING_VAR_0.typesOn?" Ignored on an Artifact created from an Artifact type.":""}
