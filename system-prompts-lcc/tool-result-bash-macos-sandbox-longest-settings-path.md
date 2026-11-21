<!--
name: 'Tool Result: macOS sandbox longest settings path'
description: Names the longest settings path with its size and source and how to fix it
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_0
  - TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_1
  - TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_2
-->
It may be the longest path in settings, which has ${TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_0.bytes} bytes and is in ${TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_1(TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_0.list)}. ${TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_0.list.isDenyList?"A parent folder can be denied in its place.":"It can be removed if it is not needed."}${TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_2([TOOL_RESULT_BASH_MACOS_SANDBOX_LONGEST_SETTINGS_PATH_VAR_0.list])}
