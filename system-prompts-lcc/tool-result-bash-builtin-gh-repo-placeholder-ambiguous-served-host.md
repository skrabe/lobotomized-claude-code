<!--
name: 'Tool result: built-in gh repo placeholder ambiguous (served hosts)'
description: >-
  Built-in gh stand-in refusal when it cannot tell which repository
  {owner}/{repo} is among the served hosts.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_SERVED_HOST_VAR_0
  - TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_SERVED_HOST_VAR_1
-->
could not tell which ${TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_SERVED_HOST_VAR_0.join(" or ")} repository {owner}/{repo} is: set GH_REPO=${TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_SERVED_HOST_VAR_1?"[HOST/]":""}OWNER/REPO or spell the repository out in the endpoint${TOOL_RESULT_BASH_BUILTIN_GH_REPO_PLACEHOLDER_AMBIGUOUS_SERVED_HOST_VAR_0.length>1?" and name its host with --hostname":""}
