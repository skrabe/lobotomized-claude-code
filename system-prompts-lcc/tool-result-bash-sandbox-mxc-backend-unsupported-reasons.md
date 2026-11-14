<!--
name: 'Tool result: Bash sandbox mxc backend unsupported reasons'
description: >-
  Init failure reason that the mxc backend cannot be used, followed by the
  joined probe reasons
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_SANDBOX_MXC_BACKEND_UNSUPPORTED_REASONS_VAR_0
-->
windows.backend is 'mxc' but ${TOOL_RESULT_BASH_SANDBOX_MXC_BACKEND_UNSUPPORTED_REASONS_VAR_0.join("; ")}
