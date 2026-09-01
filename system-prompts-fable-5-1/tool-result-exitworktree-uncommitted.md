<!--
name: ExitWorktree uncommitted work
description: >-
  ExitWorktree error returned to the model warning that removal would discard
  uncommitted work.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_EXITWORKTREE_UNCOMMITTED_VAR_0
-->
Worktree has ${TOOL_RESULT_EXITWORKTREE_UNCOMMITTED_VAR_0.join(" and ")}. Removing will discard this work permanently. Confirm with the user, then re-invoke with discard_changes: true — or use action: "keep" to preserve the worktree.
