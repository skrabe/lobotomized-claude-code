<!--
name: 'Data: Plugin error — path escapes plugin directory'
description: >-
  Plugin load error text for a component path that escapes the plugin directory,
  with optional reason, used inside the managed-plugin hooks-unknown cause
  reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_0
  - DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_1
  - DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_2
-->
Path escapes plugin directory: ${DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_0(DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_1.path)} (${DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_2(DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_1.component)})${DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_1.reason?` — ${DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_0(DATA_PLUGIN_ERROR_PATH_ESCAPES_PLUGIN_DIRECTORY_VAR_1.reason)}`:""}
