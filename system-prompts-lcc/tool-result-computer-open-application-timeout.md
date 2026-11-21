<!--
name: 'Tool result: computer open_application timed out'
description: >-
  Error when an app does not finish opening within the timeout; advises a
  screenshot before acting.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_OPEN_APPLICATION_TIMEOUT_VAR_0
-->
The app did not finish opening within ${TOOL_RESULT_COMPUTER_OPEN_APPLICATION_TIMEOUT_VAR_0/1000} seconds. It may still open, or macOS may be waiting for the user to confirm the launch, so take a screenshot before acting on the screen.
