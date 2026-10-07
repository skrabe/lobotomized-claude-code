<!--
name: 'Tool Result: Headless agent unsandboxed execution denied'
description: >-
  Permission deny message when a background agent's shell call asks for
  dangerouslyDisableSandbox, telling it not to retry.
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_HEADLESS_AGENT_UNSANDBOXED_EXECUTION_DENIED_VAR_0
-->
unsandboxed execution (dangerouslyDisableSandbox) is not available to ${TOOL_RESULT_HEADLESS_AGENT_UNSANDBOXED_EXECUTION_DENIED_VAR_0}. If the command failed with a sandbox violation, the operation cannot be performed in this context — do not retry it.
