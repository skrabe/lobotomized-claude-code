<!--
name: ExitWorktree uncommitted work
description: >-
  ExitWorktree error returned to the model warning that removal would discard
  uncommitted work.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_EXITWORKTREE_UNCOMMITTED_VAR_0
  - TOOL_RESULT_EXITWORKTREE_UNCOMMITTED_VAR_1
-->
Worktree has ${TOOL_RESULT_EXITWORKTREE_UNCOMMITTED_VAR_0.join(" and ")}. Removing will discard this work permanently.${TOOL_RESULT_EXITWORKTREE_UNCOMMITTED_VAR_1?` (Commits made in this worktree are already stored server-side, head changeset ${TOOL_RESULT_EXITWORKTREE_UNCOMMITTED_VAR_1.slice(0,12)}, and are not affected by removing it.)`:""} Confirm with the user, then re-invoke with discard_changes: true — or use action: "keep" to preserve the worktree.
