<!--
name: 'Data: Settings keys nested too deep ignored'
description: >-
  Validation message that named keys hold objects or arrays nested too deep,
  which Claude Code ignores
ccVersion: 2.1.326
variables:
  - DATA_SETTINGS_KEYS_NESTED_TOO_DEEP_IGNORED_VAR_0
  - DATA_SETTINGS_KEYS_NESTED_TOO_DEEP_IGNORED_VAR_1
  - DATA_SETTINGS_KEYS_NESTED_TOO_DEEP_IGNORED_VAR_2
-->
${DATA_SETTINGS_KEYS_NESTED_TOO_DEEP_IGNORED_VAR_0} ${DATA_SETTINGS_KEYS_NESTED_TOO_DEEP_IGNORED_VAR_1.length===1?"holds":"hold"} objects or arrays nested more than ${DATA_SETTINGS_KEYS_NESTED_TOO_DEEP_IGNORED_VAR_2} levels deep, and Claude Code ignores anything nested that deep; reduce the nesting under ${DATA_SETTINGS_KEYS_NESTED_TOO_DEEP_IGNORED_VAR_0}
