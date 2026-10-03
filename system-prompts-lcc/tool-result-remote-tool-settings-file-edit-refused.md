<!--
name: 'Remote Tool: Settings File Edit Refused'
description: >-
  Deny message for an Edit or Write from a cloud session aimed at the serving
  computer's Claude Code settings files; nothing was changed, tell the user
  those settings can only be changed on that computer.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_TOOL_SETTINGS_FILE_EDIT_REFUSED_VAR_0
-->
${TOOL_RESULT_REMOTE_TOOL_SETTINGS_FILE_EDIT_REFUSED_VAR_0} does not let a cloud session change its Claude Code settings files. Nothing was changed. Tell the user: those settings can only be changed on ${TOOL_RESULT_REMOTE_TOOL_SETTINGS_FILE_EDIT_REFUSED_VAR_0} itself.
