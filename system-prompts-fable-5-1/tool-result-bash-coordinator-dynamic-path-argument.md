<!--
name: 'Tool Result: Bash coordinator dynamic path argument'
description: >-
  Bash refusal in coordinator mode for commands whose arguments use $(…),
  variables, ~name or .. after a directory, asking for a literal path
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_COORDINATOR_DYNAMIC_PATH_ARGUMENT_VAR_0
-->
${TOOL_RESULT_BASH_COORDINATOR_DYNAMIC_PATH_ARGUMENT_VAR_0} in the coordinator does not run a command with an argument built from \`$(…)\`, a variable, a \`~name\` form, or a \`..\` after a directory name: it cannot be checked against this session's worker transcript and task output folders. Name the path literally.
