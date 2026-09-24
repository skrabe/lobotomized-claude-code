<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable, top-level directory
  scope note
description: >-
  Closing note of the unset-variable dangerous-removal message when the empty
  expansion would remove a top-level directory: the check does not fire on a
  target that cannot expand to a top-level directory. The remedy follows.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_TOP_LEVEL_DIRECTORY_SCOPE_NOTE_VAR_0
-->
This check does not fire on a target that cannot expand to a top-level directory: ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_TOP_LEVEL_DIRECTORY_SCOPE_NOTE_VAR_0(!0)}.
