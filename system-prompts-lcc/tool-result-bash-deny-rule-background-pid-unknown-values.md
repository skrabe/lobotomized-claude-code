<!--
name: 'Tool Result: deny rule matched via $! and unknown values'
description: >-
  Deny message when $! precedes any background job and empty unknowns match a
  deny rule
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_DENY_RULE_BACKGROUND_PID_UNKNOWN_VALUES_VAR_0
  - TOOL_RESULT_BASH_DENY_RULE_BACKGROUND_PID_UNKNOWN_VALUES_VAR_1
  - TOOL_RESULT_BASH_DENY_RULE_BACKGROUND_PID_UNKNOWN_VALUES_VAR_2
  - TOOL_RESULT_BASH_DENY_RULE_BACKGROUND_PID_UNKNOWN_VALUES_VAR_3
-->
Permission to use ${TOOL_RESULT_BASH_DENY_RULE_BACKGROUND_PID_UNKNOWN_VALUES_VAR_0.name} with command ${TOOL_RESULT_BASH_DENY_RULE_BACKGROUND_PID_UNKNOWN_VALUES_VAR_1.command.trim()} has been denied: the line reads $! before any background job, and with unknown values read as empty it matches the deny rule ${TOOL_RESULT_BASH_DENY_RULE_BACKGROUND_PID_UNKNOWN_VALUES_VAR_2(TOOL_RESULT_BASH_DENY_RULE_BACKGROUND_PID_UNKNOWN_VALUES_VAR_3.ruleValue)}.
