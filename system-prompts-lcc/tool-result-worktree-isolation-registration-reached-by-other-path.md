<!--
name: 'Tool Result: Worktree isolation registration reached by other path'
description: >-
  Refusal when git locates the worktree's repository at its registration via a
  different path, so its identity cannot be verified
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_0
  - TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_1
  - TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_2
  - TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_3
  - TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_4
  - TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_5
-->
Refusing to use ${TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_0} as an isolation worktree: git located its repository at ${TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_1(TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_2.gitDir,"a path not repeated here")} (common dir ${TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_1(TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_2.commonDir,"not repeated here")}), which is ${TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_3.host}'s registration of it (${TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_4(TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_5)}) reached by a different path, not the registered path itself, so its git identity could not be verified. If that path lies inside the worktree itself, treat the worktree as tampered with: run no git in it. Otherwise the usual causes are a symbolic link or junction inside ${TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_1(TOOL_RESULT_WORKTREE_ISOLATION_REGISTRATION_REACHED_BY_OTHER_PATH_VAR_3.hostCommonDir,"that checkout's git directory")} or on the way to it, or a git too old to print link-resolved paths: remove the link or update git, then retry; if neither applies, do not trust the worktree or run git in it.
