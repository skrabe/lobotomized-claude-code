<!--
name: Cloud session settings shell-write refused
description: >-
  Refuses a shell command from a cloud session that would change Claude Code's
  settings files, directing it to use Edit/Write instead so the owner can
  review.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_TOOL_SETTINGS_SHELL_WRITE_REFUSED_VAR_0
-->
${TOOL_RESULT_REMOTE_TOOL_SETTINGS_SHELL_WRITE_REFUSED_VAR_0} does not let a cloud session change its Claude Code settings files, or the folder that holds them. Nothing was run. Tell the user: those settings can only be changed on ${TOOL_RESULT_REMOTE_TOOL_SETTINGS_SHELL_WRITE_REFUSED_VAR_0} itself.
