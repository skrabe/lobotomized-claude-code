<!--
name: 'Slash Command: /plugin install marketplace headersHelper disabled by policy'
description: >-
  Install/fetch refusal when managed settings disable marketplace-declared
  commands and the marketplace's headersHelper is not declared in managed
  settings.
ccVersion: 2.1.291
variables:
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_MARKETPLACE_HEADERS_HELPER_DISABLED_BY_POLICY_VAR_0
-->
${SLASH_COMMAND_PLUGIN_INSTALL_MARKETPLACE_HEADERS_HELPER_DISABLED_BY_POLICY_VAR_0}: your organization's managed settings disable marketplace-declared commands (disableCommandPluginSources / allowManagedHooksOnly), and this marketplace's headersHelper is not declared in managed settings. The marketplace was not fetched and the command was not run; ask your admin to allow it or to declare the marketplace in managed settings.
