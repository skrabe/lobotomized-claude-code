<!--
name: 'Data: Plugin error — component path not found'
description: >-
  Plugin load error text for a missing component path (component and optional
  errno), used inside the managed-plugin hooks-unknown cause reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_0
  - DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_1
  - DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_2
-->
Path not found: ${DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_0(DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_1.path)} (${DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_2(DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_1.component)}${DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_1.errno?`, ${DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_2(DATA_PLUGIN_ERROR_PATH_NOT_FOUND_COMPONENT_VAR_1.errno)}`:""})
