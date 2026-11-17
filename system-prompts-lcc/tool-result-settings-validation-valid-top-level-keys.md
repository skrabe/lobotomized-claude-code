<!--
name: 'Tool Result: Settings validation valid top-level keys'
description: >-
  Part of the settings.json validation failure that lists the valid top-level
  settings keys when the edit changed an unknown key
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_SETTINGS_VALIDATION_VALID_TOP_LEVEL_KEYS_VAR_0
  - TOOL_RESULT_SETTINGS_VALIDATION_VALID_TOP_LEVEL_KEYS_VAR_1
-->

Valid top-level keys: ${TOOL_RESULT_SETTINGS_VALIDATION_VALID_TOP_LEVEL_KEYS_VAR_0.keys(TOOL_RESULT_SETTINGS_VALIDATION_VALID_TOP_LEVEL_KEYS_VAR_1).join(", ")}
