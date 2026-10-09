<!--
name: Nested permission request forbidden
description: Requests a separate call when a running cloud tool asks another permission.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_NESTED_PERMISSION_FORBIDDEN_VAR_0
-->
${TOOL_RESULT_SERVED_TOOL_NESTED_PERMISSION_FORBIDDEN_VAR_0.name} was not run: a tool that runs in the cloud environment cannot ask for another permission while it runs. Send it as a call of its own.
