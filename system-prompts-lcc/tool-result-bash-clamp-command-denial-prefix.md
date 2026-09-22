<!--
name: 'Tool Result: Bash Clamp Command Denial Prefix'
description: >-
  Forms the opening of the tool-result denial sent when a Bash command falls
  outside an agent's per-spawn command clamp.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_BASH_CLAMP_COMMAND_DENIAL_PREFIX_VAR_0
  - TOOL_RESULT_BASH_CLAMP_COMMAND_DENIAL_PREFIX_VAR_1
-->
Permission to use ${TOOL_RESULT_BASH_CLAMP_COMMAND_DENIAL_PREFIX_VAR_0.name} with command ${TOOL_RESULT_BASH_CLAMP_COMMAND_DENIAL_PREFIX_VAR_1.command.trim()} has been denied: this agent's Bash use is clamped to a fixed set of command forms (per-spawn bashCommandClamp), and 
