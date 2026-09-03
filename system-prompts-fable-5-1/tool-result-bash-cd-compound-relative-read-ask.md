<!--
name: 'Tool Result: Bash Cd Compound Relative Read Ask'
description: >-
  Permission-ask message when a compound command cds then reads a relative path
  that cannot be resolved while a Read() deny rule is configured.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_BASH_CD_COMPOUND_RELATIVE_READ_ASK_VAR_0
-->
${TOOL_RESULT_BASH_CD_COMPOUND_RELATIVE_READ_ASK_VAR_0} reads a file by a relative path after a cd in a compound command; which file that is cannot be resolved statically while a Read() deny rule is configured, so this needs approval.
