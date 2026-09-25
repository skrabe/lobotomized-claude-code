<!--
name: 'Data: Settings Validation allowlist invalid'
description: >-
  Settings validation issue when an allowlist setting is present but not a valid
  list: CC enforces an empty allowlist, with the setting's consequence, until it
  is fixed.
ccVersion: 2.1.282
variables:
  - DATA_SETTINGS_VALIDATION_ALLOWLIST_INVALID_EMPTY_VAR_0
  - DATA_SETTINGS_VALIDATION_ALLOWLIST_INVALID_EMPTY_VAR_1
-->
"${DATA_SETTINGS_VALIDATION_ALLOWLIST_INVALID_EMPTY_VAR_0}" was present but invalid; enforcing an empty allowlist (${DATA_SETTINGS_VALIDATION_ALLOWLIST_INVALID_EMPTY_VAR_1}) until it is fixed.
