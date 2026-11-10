<!--
name: 'Auto mode: leading cd folder no longer exists'
description: >-
  Auto-mode denial when the command begins with a cd to the shell's folder,
  which no longer exists.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_AUTO_MODE_RESTORED_CD_FOLDER_GONE_VAR_0
  - TOOL_RESULT_AUTO_MODE_RESTORED_CD_FOLDER_GONE_VAR_1
-->
${TOOL_RESULT_AUTO_MODE_RESTORED_CD_FOLDER_GONE_VAR_0} was not run: the command begins with a cd to ${TOOL_RESULT_AUTO_MODE_RESTORED_CD_FOLDER_GONE_VAR_1}, the shell's folder, which no longer exists, so it would fail. This is not a judgment that the action is unsafe. Do not issue it again as it is. Run a command that begins with a cd to a folder that exists, then go on from there. 
