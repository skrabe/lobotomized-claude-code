<!--
name: 'Tool Result: Bash [[ ]] pattern leaf standalone ]] closer'
description: >-
  Permission-analysis reason returned when a [[ ]] conditional pattern leaf may
  contain a standalone `]]` closer; surfaced to the model as the Bash
  tool_result when the resulting ask is not granted.
ccVersion: 2.1.224
-->
[[ ]] pattern leaf contains a potential standalone `]]` closer — shell cond-lexer divergence (zsh may close the conditional early)
