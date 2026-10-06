<!--
name: '/plugin install: npm registry is plain http'
description: >-
  Install refusal when a plugin's npm registry is http and not the user's
  default registry, to avoid leaking the npm token.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_NPM_REGISTRY_UNENCRYPTED_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_NPM_REGISTRY_UNENCRYPTED_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_NPM_REGISTRY_UNENCRYPTED_VAR_2
  - SLASH_COMMAND_PLUGIN_INSTALL_NPM_REGISTRY_UNENCRYPTED_VAR_3
-->
"${SLASH_COMMAND_PLUGIN_INSTALL_NPM_REGISTRY_UNENCRYPTED_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_NPM_REGISTRY_UNENCRYPTED_VAR_1(SLASH_COMMAND_PLUGIN_INSTALL_NPM_REGISTRY_UNENCRYPTED_VAR_2))}" was not fetched: its npm registry, ${SLASH_COMMAND_PLUGIN_INSTALL_NPM_REGISTRY_UNENCRYPTED_VAR_3}, is unencrypted and isn't your default npm registry, so npm could send your saved registry token to it in the clear. It works once the registry uses https (for a marketplace plugin, the marketplace's owner sets it) or is your default npm registry (npm config set registry <url>).
