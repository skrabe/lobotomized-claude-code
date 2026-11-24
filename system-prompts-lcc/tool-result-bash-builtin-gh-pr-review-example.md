<!--
name: 'Tool Result: Built-in gh PR review example'
description: >-
  Instead-of line in the built-in gh refusal for `gh pr review`: gh api
  ${}/pulls/<number>/reviews -f event=COMMENT -F body=@<text-file>  # or
  event=REQUEST_CHANGES
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_PR_REVIEW_EXAMPLE_VAR_0
-->
gh api ${TOOL_RESULT_BASH_BUILTIN_GH_PR_REVIEW_EXAMPLE_VAR_0}/pulls/<number>/reviews -f event=COMMENT -F body=@<text-file>  # or event=REQUEST_CHANGES
