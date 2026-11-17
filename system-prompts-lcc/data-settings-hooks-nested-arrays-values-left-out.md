<!--
name: 'Data: Settings hooks nested arrays values left out'
description: >-
  Fatal settings issue: hooks written as nested arrays with values nested too
  deep were left out; write hooks as an object of event names
ccVersion: 2.1.326
variables:
  - DATA_SETTINGS_HOOKS_NESTED_ARRAYS_VALUES_LEFT_OUT_VAR_0
  - DATA_SETTINGS_HOOKS_NESTED_ARRAYS_VALUES_LEFT_OUT_VAR_1
  - DATA_SETTINGS_HOOKS_NESTED_ARRAYS_VALUES_LEFT_OUT_VAR_2
-->
"hooks" is written as nested arrays and holds ${DATA_SETTINGS_HOOKS_NESTED_ARRAYS_VALUES_LEFT_OUT_VAR_0===1?"a value":`${DATA_SETTINGS_HOOKS_NESTED_ARRAYS_VALUES_LEFT_OUT_VAR_0} values`} more than ${DATA_SETTINGS_HOOKS_NESTED_ARRAYS_VALUES_LEFT_OUT_VAR_1} levels deep that ${DATA_SETTINGS_HOOKS_NESTED_ARRAYS_VALUES_LEFT_OUT_VAR_0===1?"was":"were"} left out — ${DATA_SETTINGS_HOOKS_NESTED_ARRAYS_VALUES_LEFT_OUT_VAR_2}. Write "hooks" as an object of event names.
