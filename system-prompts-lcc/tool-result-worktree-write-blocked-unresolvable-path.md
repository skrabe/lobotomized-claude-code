<!--
name: 'Tool Result: Write Blocked — Unresolvable Path Spelling'
description: >-
  Rejection message returned to the model when a write's path cannot be safely
  resolved (raw dot segment through a symlink, network-share/device-namespace
  shape, or unreadable ancestor), asking it to re-address the file by a
  plainly-spelled path.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_WORKTREE_WRITE_BLOCKED_UNRESOLVABLE_PATH_VAR_0
-->
This write was blocked because the path is spelled in a form that cannot be safely resolved (for example through a symlink storing a raw dot segment, a network-share or device-namespace shape, or an unreadable ancestor directory). ${TOOL_RESULT_WORKTREE_WRITE_BLOCKED_UNRESOLVABLE_PATH_VAR_0===void 0?"Retry the edit addressing the file by a direct, plainly-spelled path.":`If the file is inside the worktree ${TOOL_RESULT_WORKTREE_WRITE_BLOCKED_UNRESOLVABLE_PATH_VAR_0}, address it by its direct symlink-free path instead.`}
