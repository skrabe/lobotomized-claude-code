<!--
name: 'Data: Plugin error — manifest validation failed'
description: >-
  Plugin load error text listing manifest validation errors and the manifest
  path, used inside the managed-plugin hooks-unknown cause reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_MANIFEST_VALIDATION_FAILED_VAR_0
  - DATA_PLUGIN_ERROR_MANIFEST_VALIDATION_FAILED_VAR_1
  - DATA_PLUGIN_ERROR_MANIFEST_VALIDATION_FAILED_VAR_2
-->
Manifest validation failed: ${DATA_PLUGIN_ERROR_MANIFEST_VALIDATION_FAILED_VAR_0(DATA_PLUGIN_ERROR_MANIFEST_VALIDATION_FAILED_VAR_1.validationErrors.join(", "),1000)} (in ${DATA_PLUGIN_ERROR_MANIFEST_VALIDATION_FAILED_VAR_2(DATA_PLUGIN_ERROR_MANIFEST_VALIDATION_FAILED_VAR_1.manifestPath)})
