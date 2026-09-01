<!--
name: 'Tool Result: Bash Guard — declare/typeset With Autoload Flags'
description: >-
  Static bash-analysis refusal reason emitted when
  declare/typeset/local/readonly carries both -f and -u/-U; travels as the Bash
  permission-check message and is delivered to the model as the tool_result
  error content when the command isn't allowed.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_DECLARE_AUTOLOAD_FLAGS_TOO_COMPLEX_VAR_0
-->
${TOOL_RESULT_BASH_DECLARE_AUTOLOAD_FLAGS_TOO_COMPLEX_VAR_0[0]} with both -f and -u/-U flags — zsh marks a function for autoload (synonym of 'autoload'), creating a function from file contents at call time
