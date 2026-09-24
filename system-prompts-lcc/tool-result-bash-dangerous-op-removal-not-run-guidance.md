<!--
name: 'Tool Result: Bash dangerous removal not run guidance'
description: >-
  Tail of the denial for a removal blocked by the built-in safety check. It
  tells the model the command was not run, not to work around the check, to use
  a suggested safe rewrite, or to leave the removal to the user.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_REMOVAL_NOT_RUN_GUIDANCE_VAR_0
-->
The command was NOT run; do not claim it succeeded. Do not work around the check by splitting, scripting, or re-issuing the removal through another tool or shell: the check exists because a removal like this can destroy the user's data, and getting past it would not make it safe. If the text below suggests a safe rewrite, run that instead; it goes through the same check. Otherwise finish the rest of the task without this removal, tell the user what you wanted to delete and why, and leave the removal to them. What was flagged: ${TOOL_RESULT_BASH_DANGEROUS_OP_REMOVAL_NOT_RUN_GUIDANCE_VAR_0}
