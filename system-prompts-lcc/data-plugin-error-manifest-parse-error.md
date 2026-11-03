<!--
name: 'Data: Plugin error — manifest parse error'
description: >-
  Plugin load error text giving the manifest parse error and manifest path, used
  inside the managed-plugin hooks-unknown cause reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_MANIFEST_PARSE_ERROR_VAR_0
  - DATA_PLUGIN_ERROR_MANIFEST_PARSE_ERROR_VAR_1
  - DATA_PLUGIN_ERROR_MANIFEST_PARSE_ERROR_VAR_2
-->
Manifest parse error: ${DATA_PLUGIN_ERROR_MANIFEST_PARSE_ERROR_VAR_0(DATA_PLUGIN_ERROR_MANIFEST_PARSE_ERROR_VAR_1.parseError,500)} (in ${DATA_PLUGIN_ERROR_MANIFEST_PARSE_ERROR_VAR_2(DATA_PLUGIN_ERROR_MANIFEST_PARSE_ERROR_VAR_1.manifestPath)})
