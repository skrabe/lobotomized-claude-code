<!--
name: 'Tool Result: Built-in gh PR create example'
description: >-
  Instead-of line in the built-in gh refusal for `gh pr create`: gh api
  ${}/pulls -F title=@<title-file> -f head='<branch>' -f base='<base branch>' -F
  body=@<text-file>
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_PR_CREATE_EXAMPLE_VAR_0
-->
gh api ${TOOL_RESULT_BASH_BUILTIN_GH_PR_CREATE_EXAMPLE_VAR_0}/pulls -F title=@<title-file> -f head='<branch>' -f base='<base branch>' -F body=@<text-file>  # a draft: add -F draft=true
