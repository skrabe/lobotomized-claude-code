<!--
name: 'Tool description: Bash Git Bash path conversion note'
description: >-
  Windows Git Bash note on /tmp and /c path conversion only in arguments, not
  inside scripts or inline code.
ccVersion: 2.1.332
variables:
  - TOOL_DESCRIPTION_BASH_GIT_BASH_PATH_CONVERSION_NOTE_VAR_0
  - TOOL_DESCRIPTION_BASH_GIT_BASH_PATH_CONVERSION_NOTE_VAR_1
-->
Git Bash converts \`/tmp/...\` and \`/c/...\` paths for Windows programs such as python and node only in arguments and environment variables, not inside a script, a heredoc or inline code, even where \`$HOME\` or \`$(pwd)\` put them there. Inside code, use a relative path or a drive path such as \`C:/...\`, or pass the path as an argument. \`/tmp\` is usually not \`C:/tmp\`. Do not give \`/tmp/...\` paths to ${TOOL_DESCRIPTION_BASH_GIT_BASH_PATH_CONVERSION_NOTE_VAR_0} or ${TOOL_DESCRIPTION_BASH_GIT_BASH_PATH_CONVERSION_NOTE_VAR_1}, which look for them on the current drive.
