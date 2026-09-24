<!--
name: 'Data: Settings Validation Attribution Expected Boolean Or Object'
description: >-
  Settings validation error for the attribution key when it is neither a boolean
  nor an object, naming the received type; part of the settings validation
  failure the model reads after a failed settings edit.
ccVersion: 2.1.281
variables:
  - DATA_SETTINGS_VALIDATION_ATTRIBUTION_EXPECTED_BOOLEAN_OR_OBJECT_VAR_0
  - DATA_SETTINGS_VALIDATION_ATTRIBUTION_EXPECTED_BOOLEAN_OR_OBJECT_VAR_1
-->
Expected false, true, or an object such as { "commit": "", "pr": "" }, but received ${DATA_SETTINGS_VALIDATION_ATTRIBUTION_EXPECTED_BOOLEAN_OR_OBJECT_VAR_0.isArray(DATA_SETTINGS_VALIDATION_ATTRIBUTION_EXPECTED_BOOLEAN_OR_OBJECT_VAR_1.input)?"array":DATA_SETTINGS_VALIDATION_ATTRIBUTION_EXPECTED_BOOLEAN_OR_OBJECT_VAR_1.input===null?"null":typeof DATA_SETTINGS_VALIDATION_ATTRIBUTION_EXPECTED_BOOLEAN_OR_OBJECT_VAR_1.input}
