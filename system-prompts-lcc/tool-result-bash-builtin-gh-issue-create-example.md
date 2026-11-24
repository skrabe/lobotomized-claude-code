<!--
name: 'Tool Result: Built-in gh Issue create example'
description: >-
  Instead-of line in the built-in gh refusal for `gh issue create`: gh api
  ${}/issues -F title=@<title-file> -F body=@<text-file>
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_ISSUE_CREATE_EXAMPLE_VAR_0
-->
gh api ${TOOL_RESULT_BASH_BUILTIN_GH_ISSUE_CREATE_EXAMPLE_VAR_0}/issues -F title=@<title-file> -F body=@<text-file>
