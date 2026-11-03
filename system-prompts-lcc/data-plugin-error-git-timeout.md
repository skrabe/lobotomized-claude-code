<!--
name: 'Data: Plugin error — git operation timeout'
description: >-
  Plugin load error text for a git operation that timed out on a URL, used
  inside the managed-plugin hooks-unknown cause reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_GIT_TIMEOUT_VAR_0
  - DATA_PLUGIN_ERROR_GIT_TIMEOUT_VAR_1
  - DATA_PLUGIN_ERROR_GIT_TIMEOUT_VAR_2
-->
Git ${DATA_PLUGIN_ERROR_GIT_TIMEOUT_VAR_0(DATA_PLUGIN_ERROR_GIT_TIMEOUT_VAR_1.operation)} timeout: ${DATA_PLUGIN_ERROR_GIT_TIMEOUT_VAR_2(DATA_PLUGIN_ERROR_GIT_TIMEOUT_VAR_1.gitUrl)}
