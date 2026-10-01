<!--
name: 'Device tool refused: sandbox weakened'
description: >-
  Refusal message for a served device-tool call explaining the device's sandbox
  is configured with a setting that weakens its isolation, so the device serves
  no device tools; tell the user, do not retry in a loop.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_DEVICE_TOOL_SERVE_REFUSED_SANDBOX_WEAKENED_VAR_0
-->
${TOOL_RESULT_DEVICE_TOOL_SERVE_REFUSED_SANDBOX_WEAKENED_VAR_0} refused: the sandbox on this device is configured with a setting that weakens its isolation (sandbox.allowAppleEvents, sandbox.enableWeakerNestedSandbox, sandbox.enableWeakerNetworkIsolation, sandbox.network.allowLocalBinding, sandbox.network.allowMachLookup, or a sandbox.ripgrep override outside managed policy settings), so this device serves no device tools. Tell the user; do not retry in a loop.
