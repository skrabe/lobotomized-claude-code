<!--
name: 'Tool Result: Built-in gh PR head sha example'
description: >-
  Example gh api pulls/<number> call in the pr checks guidance, noting head.sha
  is the <sha> for the check-runs call.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_PR_HEAD_SHA_EXAMPLE_VAR_0
-->
gh api ${TOOL_RESULT_BASH_BUILTIN_GH_PR_HEAD_SHA_EXAMPLE_VAR_0}/pulls/<number>  # <sha> of a pull request: its head.sha
