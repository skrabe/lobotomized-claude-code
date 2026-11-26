<!--
name: 'Plugin error: plugin not cached'
description: >-
  Plugin error message for a plugin-cache-miss: the plugin is not cached at its
  install path and /reload-plugins should be run.
ccVersion: 2.1.332
variables:
  - DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_0
  - DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_1
  - DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_2
-->
Plugin "${DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_0(DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_1.plugin)}" not cached at ${DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_2(DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_1.installPath)} — run /reload-plugins to refresh${DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_1.installedListHeldNote===void 0?"":`. ${DATA_PLUGIN_ERROR_PLUGIN_NOT_CACHED_VAR_1.installedListHeldNote}`}
