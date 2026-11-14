<!--
name: 'Tool Result: Prompt shell untrusted bare repo git blocked'
description: >-
  Error when a skill's shell command could not run because the folder looks like
  an untrusted bare git repository, suggesting allowing the git commands via
  /permissions
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_PROMPT_SHELL_UNTRUSTED_BARE_REPO_GIT_BLOCKED_VAR_0
  - TOOL_RESULT_PROMPT_SHELL_UNTRUSTED_BARE_REPO_GIT_BLOCKED_VAR_1
-->
Couldn't run \`${TOOL_RESULT_PROMPT_SHELL_UNTRUSTED_BARE_REPO_GIT_BLOCKED_VAR_0}\` for ${TOOL_RESULT_PROMPT_SHELL_UNTRUSTED_BARE_REPO_GIT_BLOCKED_VAR_1}. This folder or one above it looks like a bare git repository that may not be yours, and git can run commands named in a repository's files. If you trust this folder, allow the git commands this needs, for example with /permissions, and try again.
