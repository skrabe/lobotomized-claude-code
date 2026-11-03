<!--
name: 'Data: Plugin error — enabled in project settings but not installed'
description: >-
  Plugin load error text for a plugin enabled in project settings but not
  installed, with the install command to run, used inside the managed-plugin
  hooks-unknown cause reported by /model
ccVersion: 2.1.317
variables:
  - DATA_PLUGIN_ERROR_ENABLED_IN_PROJECT_NOT_INSTALLED_VAR_0
  - DATA_PLUGIN_ERROR_ENABLED_IN_PROJECT_NOT_INSTALLED_VAR_1
  - DATA_PLUGIN_ERROR_ENABLED_IN_PROJECT_NOT_INSTALLED_VAR_2
-->
Plugin "${DATA_PLUGIN_ERROR_ENABLED_IN_PROJECT_NOT_INSTALLED_VAR_0(DATA_PLUGIN_ERROR_ENABLED_IN_PROJECT_NOT_INSTALLED_VAR_1.plugin)}" is enabled in project settings but isn't installed${DATA_PLUGIN_ERROR_ENABLED_IN_PROJECT_NOT_INSTALLED_VAR_2?` — run \`${DATA_PLUGIN_ERROR_ENABLED_IN_PROJECT_NOT_INSTALLED_VAR_2}\``:" — install it at project scope (from /plugin or claude plugin install)"}
