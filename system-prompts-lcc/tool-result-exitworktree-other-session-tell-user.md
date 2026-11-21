<!--
name: 'Tool Result: ExitWorktree tell user about other session'
description: >-
  Tells Claude to name the session using the worktree and not end it or remove
  the worktree by shell
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_EXITWORKTREE_OTHER_SESSION_TELL_USER_VAR_0
-->
${TOOL_RESULT_EXITWORKTREE_OTHER_SESSION_TELL_USER_VAR_0===""?"":`${TOOL_RESULT_EXITWORKTREE_OTHER_SESSION_TELL_USER_VAR_0} `}Tell the user which session is using the worktree${TOOL_RESULT_EXITWORKTREE_OTHER_SESSION_TELL_USER_VAR_0===""?"":" and what ends it"}. Do not end that session yourself, and do not remove the worktree with a shell command while it is running.
