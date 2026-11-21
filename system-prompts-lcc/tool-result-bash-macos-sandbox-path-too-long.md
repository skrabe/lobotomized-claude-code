<!--
name: 'Tool Result: macOS sandbox path too long'
description: >-
  Bash result when one sandbox rule path exceeds the macOS limit, telling the
  model sandboxed commands will keep failing and to tell the user
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_TOO_LONG_VAR_0
  - TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_TOO_LONG_VAR_1
-->
${TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_TOO_LONG_VAR_0} one path in the sandbox's rules is longer than macOS accepts (about 1,000 characters, fewer for a pattern with many wildcards). Sandboxed commands will keep failing until this is fixed, so tell the user. ${TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_TOO_LONG_VAR_1}
