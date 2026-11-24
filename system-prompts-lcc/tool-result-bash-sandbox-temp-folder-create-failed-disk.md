<!--
name: 'Tool result: sandbox temp folder create failed (disk)'
description: >-
  Bash tool error explaining the sandbox could not create a protected temp
  folder because the temp disk is full/over quota/failing, so the command was
  not started.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_BASH_SANDBOX_TEMP_FOLDER_CREATE_FAILED_DISK_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_TEMP_FOLDER_CREATE_FAILED_DISK_VAR_1
-->
The sandbox could not create ${TOOL_RESULT_BASH_SANDBOX_TEMP_FOLDER_CREATE_FAILED_DISK_VAR_0()}, a folder it must protect from the command, because the temp disk is full, over its quota or failing (${TOOL_RESULT_BASH_SANDBOX_TEMP_FOLDER_CREATE_FAILED_DISK_VAR_1}). The sandbox may let this command write the temp folder, so the command was not started. Make room on the temp disk, or repair it, then run the command again.
