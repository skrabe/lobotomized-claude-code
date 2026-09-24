<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable, filesystem-root scope
  note
description: >-
  Closing note of the unset-variable dangerous-removal message when no top-level
  child is involved: the check does not fire on a target that cannot expand to
  the filesystem root. The remedy follows.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_FILESYSTEM_ROOT_SCOPE_NOTE_VAR_0
-->
This check does not fire on a target that cannot expand to the filesystem root: ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_FILESYSTEM_ROOT_SCOPE_NOTE_VAR_0(!0)}.
