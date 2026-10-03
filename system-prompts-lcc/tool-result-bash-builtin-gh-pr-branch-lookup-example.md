<!--
name: 'Tool Result: Built-in gh PR-for-branch lookup example'
description: >-
  Example gh api call (const F) listing pulls by head branch to find the current
  branch's pull request, shown in instead-of guidance for pr commands.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_PR_BRANCH_LOOKUP_EXAMPLE_VAR_0
-->
gh api '${TOOL_RESULT_BASH_BUILTIN_GH_PR_BRANCH_LOOKUP_EXAMPLE_VAR_0}/pulls?head={owner}:{branch}&state=all'  # <number> of the current branch's pull request (a fork's: its owner in place of {owner} before the colon)
