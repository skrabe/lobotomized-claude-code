<!--
name: 'Data: Plugin error — git authentication failed'
description: >-
  Plugin load error text naming the git auth type and URL that failed, used
  inside the managed-plugin hooks-unknown cause reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_GIT_AUTH_FAILED_VAR_0
  - DATA_PLUGIN_ERROR_GIT_AUTH_FAILED_VAR_1
  - DATA_PLUGIN_ERROR_GIT_AUTH_FAILED_VAR_2
-->
Git authentication failed (${DATA_PLUGIN_ERROR_GIT_AUTH_FAILED_VAR_0(DATA_PLUGIN_ERROR_GIT_AUTH_FAILED_VAR_1.authType)}): ${DATA_PLUGIN_ERROR_GIT_AUTH_FAILED_VAR_2(DATA_PLUGIN_ERROR_GIT_AUTH_FAILED_VAR_1.gitUrl)}
