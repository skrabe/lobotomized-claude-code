<!--
name: 'Tool Result: Built-in gh Issue edit example'
description: >-
  Instead-of line in the built-in gh refusal for `gh issue edit`: gh api -X
  PATCH ${}/issues/<number> -F title=@<title-file> -F body=@<text-file>
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_ISSUE_EDIT_EXAMPLE_VAR_0
-->
gh api -X PATCH ${TOOL_RESULT_BASH_BUILTIN_GH_ISSUE_EDIT_EXAMPLE_VAR_0}/issues/<number> -F title=@<title-file> -F body=@<text-file>
