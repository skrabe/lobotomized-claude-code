<!--
name: 'Tool Result: Built-in gh Release create example'
description: >-
  Instead-of line in the built-in gh refusal for `gh release create`: gh api
  ${}/releases -f tag_name=<tag> -F name=@<title-file> -F body=@<text-file>  #
  proxy may refuse release writes
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_RELEASE_CREATE_EXAMPLE_VAR_0
-->
gh api ${TOOL_RESULT_BASH_BUILTIN_GH_RELEASE_CREATE_EXAMPLE_VAR_0}/releases -f tag_name=<tag> -F name=@<title-file> -F body=@<text-file>  # this session's GitHub proxy may refuse release writes
