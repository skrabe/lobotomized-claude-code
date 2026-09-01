<!--
name: Working-directory-changed notice
description: >-
  System reminder enqueued as modelMessage into the conversation when the
  session cwd changes via /cd or set_cwd, telling the model the environment
  block is stale.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_VAR_0
  - SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_VAR_1
-->
The session's working directory has changed to ${SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_VAR_0} (${SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_VAR_1==="cd_command"?"via /cd":"by the user"}). The environment block at the start of this conversation still names the 
