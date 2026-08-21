<!--
name: 'Tool Result: Artifact Verify Capture Unreadable'
description: >-
  Verify tool_result when diagnostics were captured but none could be read into
  the result, so the render is unobserved.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_1
  - TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_2
  - TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_3
-->
A viewer loaded ${TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_0} (version ${TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_1}) and diagnostics WERE captured, but none could be read into this result (${TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_2>0?`${TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_2} ${TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_3(TOOL_RESULT_ARTIFACT_VERIFY_CAPTURE_UNREADABLE_VAR_2,"entry","entries")} dropped over the size cap`:"server-truncated to zero"}). Treat the render as unobserved.
