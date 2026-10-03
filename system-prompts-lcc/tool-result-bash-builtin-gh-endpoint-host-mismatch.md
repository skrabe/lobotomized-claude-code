<!--
name: 'Tool Result: Built-in gh endpoint host mismatch'
description: >-
  Refusal when an endpoint URL is not on the host the gh sends requests to,
  giving an example REST path.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_ENDPOINT_HOST_MISMATCH_VAR_0
-->
this gh sends requests to ${TOOL_RESULT_BASH_BUILTIN_GH_ENDPOINT_HOST_MISMATCH_VAR_0.replace("https://","")} only; give a REST path such as repos/{owner}/{repo}/pulls
