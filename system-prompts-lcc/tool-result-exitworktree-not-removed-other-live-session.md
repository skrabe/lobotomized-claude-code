<!--
name: 'Tool Result: ExitWorktree not removed for other live session'
description: Error when another live session in the worktree stops removal
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_OTHER_LIVE_SESSION_VAR_0
  - TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_OTHER_LIVE_SESSION_VAR_1
  - TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_OTHER_LIVE_SESSION_VAR_2
-->
Worktree not removed, and this session is still in it: another Claude Code session (${TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_OTHER_LIVE_SESSION_VAR_0(TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_OTHER_LIVE_SESSION_VAR_1)}) is running in the worktree, though it may be idle. If the user ends that session, call this tool again. Otherwise use action: "keep" to leave the worktree in place. ${TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_OTHER_LIVE_SESSION_VAR_2(TOOL_RESULT_EXITWORKTREE_NOT_REMOVED_OTHER_LIVE_SESSION_VAR_1)}
