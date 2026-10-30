<!--
name: 'Tool Result: worktree guard computed value in single-value slot'
description: >-
  Worktree guard operand detail that a computed value where one value belongs
  may split, with quoting guidance
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_COMPUTED_SINGLE_VALUE_SLOT_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_COMPUTED_SINGLE_VALUE_SLOT_VAR_1
-->
with ${TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_COMPUTED_SINGLE_VALUE_SLOT_VAR_0(TOOL_RESULT_BASH_WORKTREE_GUARD_OPERAND_COMPUTED_SINGLE_VALUE_SLOT_VAR_1)} where one value belongs: it may become no word or several, and the words after it may then be read as variable names (write it as one double-quoted variable, such as "$NAME", or as quoted text; $@, $*, [@], [*] and \${! are refused here even inside quotes)
