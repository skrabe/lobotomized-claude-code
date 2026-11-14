<!--
name: Background session isolation guard
description: >-
  Edit/Write validation error returned to the model when a background session
  hasn't isolated its changes yet.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BG_SESSION_ISOLATION_GUARD_VAR_0
  - TOOL_RESULT_BG_SESSION_ISOLATION_GUARD_VAR_1
-->
This background session hasn't isolated its changes yet. Call ${TOOL_RESULT_BG_SESSION_ISOLATION_GUARD_VAR_0} first so edits land in a worktree instead of the shared checkout, then retry this edit using the worktree path${TOOL_RESULT_BG_SESSION_ISOLATION_GUARD_VAR_1?` (a path inside a linked git worktree is accepted; enter one that you made yourself with ${TOOL_RESULT_BG_SESSION_ISOLATION_GUARD_VAR_0} and its \`path\`)`:""}. (To disable this guard for this repo, set \`"worktree": {"bgIsolation": "none"}\` in .claude/settings.json.)
