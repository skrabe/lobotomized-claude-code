<!--
name: 'Tool Result: Bash Keyword Glued To Paren Too Complex'
description: >-
  Too-complex reason when a shell keyword is glued to a paren so zsh would
  glob-expand the group.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_KEYWORD_GLUED_TO_PAREN_TOO_COMPLEX_VAR_0
-->
\`${TOOL_RESULT_BASH_KEYWORD_GLUED_TO_PAREN_TOO_COMPLEX_VAR_0.type}\` glued to a paren — bash reads a keyword and a subshell, but zsh reads one glob-group word and expands its contents
