<!--
name: 'Data: Plugin error — network error'
description: >-
  Plugin load error text for a network failure on a URL with optional details,
  used inside the managed-plugin hooks-unknown cause reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_NETWORK_ERROR_VAR_0
  - DATA_PLUGIN_ERROR_NETWORK_ERROR_VAR_1
  - DATA_PLUGIN_ERROR_NETWORK_ERROR_VAR_2
-->
Network error: ${DATA_PLUGIN_ERROR_NETWORK_ERROR_VAR_0(DATA_PLUGIN_ERROR_NETWORK_ERROR_VAR_1.url)}${DATA_PLUGIN_ERROR_NETWORK_ERROR_VAR_1.details?` - ${DATA_PLUGIN_ERROR_NETWORK_ERROR_VAR_2(DATA_PLUGIN_ERROR_NETWORK_ERROR_VAR_1.details)}`:""}
