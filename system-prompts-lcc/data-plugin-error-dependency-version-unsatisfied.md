<!--
name: 'Data: Plugin error — dependency version unsatisfied'
description: >-
  Plugin load error text giving the required and installed dependency versions,
  used inside the managed-plugin hooks-unknown cause reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_DEPENDENCY_VERSION_UNSATISFIED_VAR_0
  - DATA_PLUGIN_ERROR_DEPENDENCY_VERSION_UNSATISFIED_VAR_1
-->
Requires "${DATA_PLUGIN_ERROR_DEPENDENCY_VERSION_UNSATISFIED_VAR_0(DATA_PLUGIN_ERROR_DEPENDENCY_VERSION_UNSATISFIED_VAR_1.dependency)}" ${DATA_PLUGIN_ERROR_DEPENDENCY_VERSION_UNSATISFIED_VAR_0(DATA_PLUGIN_ERROR_DEPENDENCY_VERSION_UNSATISFIED_VAR_1.required)}, installed ${DATA_PLUGIN_ERROR_DEPENDENCY_VERSION_UNSATISFIED_VAR_0(DATA_PLUGIN_ERROR_DEPENDENCY_VERSION_UNSATISFIED_VAR_1.installed??"version unknown")}
