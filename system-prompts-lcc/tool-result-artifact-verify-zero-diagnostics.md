<!--
name: 'Tool Result: Artifact Verify Zero Diagnostics'
description: >-
  Verify tool_result when a viewer loaded the version and capture recorded zero
  diagnostics, a good signal but not proof.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_VERIFY_ZERO_DIAGNOSTICS_VAR_0
  - TOOL_RESULT_ARTIFACT_VERIFY_ZERO_DIAGNOSTICS_VAR_1
-->
A viewer loaded ${TOOL_RESULT_ARTIFACT_VERIFY_ZERO_DIAGNOSTICS_VAR_0} (version ${TOOL_RESULT_ARTIFACT_VERIFY_ZERO_DIAGNOSTICS_VAR_1}) and zero diagnostics were captured: no console output, uncaught errors, failed resource loads, or failed capability calls reached the capture. Capture is cooperative and bounded — a good signal, not proof of correctness.
