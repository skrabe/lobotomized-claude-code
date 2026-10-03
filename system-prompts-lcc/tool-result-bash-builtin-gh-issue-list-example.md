<!--
name: 'Tool Result: Built-in gh issue list example'
description: >-
  Example gh api issues call for gh issue list, warning that pull requests
  appear in the list with a pull_request key.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_ISSUE_LIST_EXAMPLE_VAR_0
-->
gh api '${TOOL_RESULT_BASH_BUILTIN_GH_ISSUE_LIST_EXAMPLE_VAR_0}/issues?state=open&per_page=100'  # pull requests are in the list too: each has a pull_request key
