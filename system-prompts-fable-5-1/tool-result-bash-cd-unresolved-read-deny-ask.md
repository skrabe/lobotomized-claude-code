<!--
name: Bash Cd Unresolved Read Deny Ask
description: >-
  Permission-ask message when a command after an unresolvable cd would search
  under a configured Read() deny rule.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_BASH_CD_UNRESOLVED_READ_DENY_ASK_VAR_0
  - TOOL_RESULT_BASH_CD_UNRESOLVED_READ_DENY_ASK_VAR_1
-->
${TOOL_RESULT_BASH_CD_UNRESOLVED_READ_DENY_ASK_VAR_0} on '${TOOL_RESULT_BASH_CD_UNRESOLVED_READ_DENY_ASK_VAR_1}' after a cd would search a directory that cannot be determined here, and a Read() deny rule is configured; only you can approve running it anyway.
