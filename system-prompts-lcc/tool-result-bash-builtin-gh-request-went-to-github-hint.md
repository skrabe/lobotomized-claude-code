<!--
name: 'Tool Result: Built-in gh request went to github.com hint'
description: >-
  Stderr hint after a 401/403/404 that the request went to github.com and how to
  target another host via --hostname or a repos/{owner}/{repo} endpoint.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_REQUEST_WENT_TO_GITHUB_HINT_VAR_0
  - TOOL_RESULT_BASH_BUILTIN_GH_REQUEST_WENT_TO_GITHUB_HINT_VAR_1
-->
this request went to ${TOOL_RESULT_BASH_BUILTIN_GH_REQUEST_WENT_TO_GITHUB_HINT_VAR_0}; for a repository on ${TOOL_RESULT_BASH_BUILTIN_GH_REQUEST_WENT_TO_GITHUB_HINT_VAR_1.join(" or ")}, add --hostname <host> or write the endpoint as repos/{owner}/{repo}/...
