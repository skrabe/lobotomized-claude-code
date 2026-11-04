<!--
name: 'REPL: Dangerous Removal Not Run'
description: >-
  Deny message for a REPL shell command whose removal target resolves through a
  variable or relative path; asks for a full path.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_DANGEROUS_REMOVAL_NOT_RUN_VAR_0
-->
This command was not run. ${TOOL_RESULT_REPL_DANGEROUS_REMOVAL_NOT_RUN_VAR_0}.
If you mean to remove it, write the full path in the command itself, not a shell variable or a relative path. The command then gets the normal permission check.
