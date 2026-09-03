<!--
name: 'Tool Result: Artifact Verify No Viewer'
description: >-
  Verify tool_result when no runtime diagnostics are readable because no viewer
  loaded the version, which is not a clean render.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_VERIFY_NO_VIEWER_VAR_0
  - TOOL_RESULT_ARTIFACT_VERIFY_NO_VIEWER_VAR_1
  - TOOL_RESULT_ARTIFACT_VERIFY_NO_VIEWER_VAR_2
-->
No runtime diagnostics readable for ${TOOL_RESULT_ARTIFACT_VERIFY_NO_VIEWER_VAR_0} (version ${TOOL_RESULT_ARTIFACT_VERIFY_NO_VIEWER_VAR_1}): no viewer has loaded this version in the last 24h${TOOL_RESULT_ARTIFACT_VERIFY_NO_VIEWER_VAR_2.waited?" (checked twice over ~3 seconds)":""}, or the diagnostics are not readable for this artifact (they are owner-only). This is NOT evidence of a clean render — open the page (or ask the user to open it) and verify again.
