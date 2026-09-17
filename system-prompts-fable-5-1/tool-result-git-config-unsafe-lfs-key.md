<!--
name: 'Tool Result: Git Config Unsafe Lfs Key'
description: >-
  Explains git was not run because repo config names a git-lfs program that
  would run on checkout and status.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_GIT_CONFIG_UNSAFE_LFS_KEY_VAR_0
  - TOOL_RESULT_GIT_CONFIG_UNSAFE_LFS_KEY_VAR_1
-->
the repository's own git config sets ${TOOL_RESULT_GIT_CONFIG_UNSAFE_LFS_KEY_VAR_0.lfsKey===void 0?TOOL_RESULT_GIT_CONFIG_UNSAFE_LFS_KEY_VAR_0.key:`${TOOL_RESULT_GIT_CONFIG_UNSAFE_LFS_KEY_VAR_0.key}, an entry git-lfs reads as ${TOOL_RESULT_GIT_CONFIG_UNSAFE_LFS_KEY_VAR_0.lfsKey}`}, which names a program git-lfs would run for any LFS path, on checkout and on status alike (${TOOL_RESULT_GIT_CONFIG_UNSAFE_LFS_KEY_VAR_1})
