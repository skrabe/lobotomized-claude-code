<!--
name: 'Data: Plugin error — dependency not installed, check its marketplace'
description: >-
  Says a plugin dependency is not installed and tells the reader to run the
  install command, or check that its marketplace is added.
ccVersion: 2.1.318
variables:
  - DATA_PLUGIN_ERROR_DEPENDENCY_NOT_INSTALLED_CHECK_MARKETPLACE_VAR_0
  - DATA_PLUGIN_ERROR_DEPENDENCY_NOT_INSTALLED_CHECK_MARKETPLACE_VAR_1
  - DATA_PLUGIN_ERROR_DEPENDENCY_NOT_INSTALLED_CHECK_MARKETPLACE_VAR_2
-->
not installed — ${DATA_PLUGIN_ERROR_DEPENDENCY_NOT_INSTALLED_CHECK_MARKETPLACE_VAR_0.sameNameSyncedPlugin===void 0?"":`${DATA_PLUGIN_ERROR_DEPENDENCY_NOT_INSTALLED_CHECK_MARKETPLACE_VAR_1(DATA_PLUGIN_ERROR_DEPENDENCY_NOT_INSTALLED_CHECK_MARKETPLACE_VAR_0.sameNameSyncedPlugin)}; `}${DATA_PLUGIN_ERROR_DEPENDENCY_NOT_INSTALLED_CHECK_MARKETPLACE_VAR_2?`run \`${DATA_PLUGIN_ERROR_DEPENDENCY_NOT_INSTALLED_CHECK_MARKETPLACE_VAR_2}\`, or `:""}check that its marketplace is added
