<!--
name: 'Data: Plugin error — path not found'
description: >-
  Plugin load error text for a missing path with optional errno, used inside the
  managed-plugin hooks-unknown cause that /model reports when PreModelSwitch
  hooks could not be checked
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_PATH_NOT_FOUND_VAR_0
  - DATA_PLUGIN_ERROR_PATH_NOT_FOUND_VAR_1
  - DATA_PLUGIN_ERROR_PATH_NOT_FOUND_VAR_2
-->
Path not found: ${DATA_PLUGIN_ERROR_PATH_NOT_FOUND_VAR_0(DATA_PLUGIN_ERROR_PATH_NOT_FOUND_VAR_1.path)}${DATA_PLUGIN_ERROR_PATH_NOT_FOUND_VAR_1.errno?` (${DATA_PLUGIN_ERROR_PATH_NOT_FOUND_VAR_2(DATA_PLUGIN_ERROR_PATH_NOT_FOUND_VAR_1.errno)})`:""}
