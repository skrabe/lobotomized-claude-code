<!--
name: 'Tool Result: Bash Guard — Wrapped Declare With Autoload Flags'
description: >-
  Static bash-analysis refusal reason when declare/typeset/readonly reached as a
  plain command through a wrapper or quoting carries both -f and -u/-U;
  delivered to the model as the Bash tool_result error content.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_WRAPPED_AUTOLOAD_FLAGS_NOT_ANALYZABLE_VAR_0
-->
'${TOOL_RESULT_BASH_WRAPPED_AUTOLOAD_FLAGS_NOT_ANALYZABLE_VAR_0}' with both -f and -u/-U flags (reached as plain command via wrapper/quote) — zsh marks a function for autoload (synonym of 'autoload')
