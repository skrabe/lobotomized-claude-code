<!--
name: 'Data: Settings validation block not an object, locks restrictive'
description: >-
  Settings load error when a settings block was not an object and its locks are
  treated as their restrictive values
ccVersion: 2.1.282
variables:
  - DATA_SETTINGS_VALIDATION_NOT_OBJECT_LOCKS_RESTRICTIVE_VAR_0
  - DATA_SETTINGS_VALIDATION_NOT_OBJECT_LOCKS_RESTRICTIVE_VAR_1
-->
"${DATA_SETTINGS_VALIDATION_NOT_OBJECT_LOCKS_RESTRICTIVE_VAR_0}" was present but not an object; treating its locks as their restrictive values (${DATA_SETTINGS_VALIDATION_NOT_OBJECT_LOCKS_RESTRICTIVE_VAR_1.join(", ")}) until it is fixed.
