<!--
name: 'Tool Result: macOS sandbox path lists too long'
description: >-
  Bash result when the sandbox path lists exceed macOS total size, with the deny
  count and what to shorten
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_0
  - TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_1
  - TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_2
  - TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_3
  - TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_4
-->
${TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_0} the sandbox's lists of paths are ${TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_1.cause==="lists_probably_too_long"?"probably ":""}too long for macOS, which limits their total size. Sandboxed commands will keep failing until this is fixed, so tell the user. The sandbox denies ${TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_2.length} paths${TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_3}.${TOOL_RESULT_BASH_MACOS_SANDBOX_PATH_LISTS_TOO_LONG_VAR_4}
