<!--
name: 'Tool result: built-in gh repo placeholder ambiguous (any host)'
description: >-
  Built-in gh stand-in refusal when it cannot tell which repository
  {owner}/{repo} is, from findOnAnyHost.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_ANY_HOST_VAR_0
-->
could not tell which ${TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_ANY_HOST_VAR_0===void 0?"":`${TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_ANY_HOST_VAR_0} `}repository {owner}/{repo} is: set GH_REPO=OWNER/REPO or spell the repository out in the endpoint${TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_ANY_HOST_VAR_0===void 0?" and name its host with --hostname":""}
