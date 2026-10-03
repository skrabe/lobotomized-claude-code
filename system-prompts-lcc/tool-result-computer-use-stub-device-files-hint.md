<!--
name: 'Tool Result: Enable stub device-files hint'
description: >-
  Hint appended to the enable-stub tool results telling Claude to use
  device_list_dir style device tools for files on the user's computer, or say
  they cannot be reached.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_COMPUTER_USE_STUB_DEVICE_FILES_HINT_VAR_0
-->
If the request is about files or folders on the user's computer and you have device tools here (loaded or through tool search), such as mcp__${TOOL_RESULT_COMPUTER_USE_STUB_DEVICE_FILES_HINT_VAR_0}__device_list_dir, use them for that part; if it is and you have none, tell the user that files on their computer can't be reached right now.
