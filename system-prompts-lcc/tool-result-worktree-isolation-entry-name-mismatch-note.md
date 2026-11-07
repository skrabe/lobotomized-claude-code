<!--
name: 'Tool Result: Worktree isolation entry name mismatch note'
description: >-
  Note that the worktree entry's name differs from this worktree's and should
  not be re-linked
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_2
-->
${TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_0(TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_1)&&TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_0(TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_2)?` That entry is named ${TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_1}, not ${TOOL_RESULT_WORKTREE_ISOLATION_ENTRY_NAME_MISMATCH_NOTE_VAR_2}.`:" That entry's name is not this worktree's."} If that entry is another worktree of yours, it is its own, whatever it names now — do not re-link it.
