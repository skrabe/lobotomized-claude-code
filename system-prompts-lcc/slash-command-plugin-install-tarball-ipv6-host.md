<!--
name: 'Slash Command: Plugin Install Tarball IPv6 Host'
description: >-
  Refusal when an npm plugin tarball downloads from an IPv6 spelling of an IPv4
  address that the organization plugin source rules cannot check
ccVersion: 2.1.285
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_TARBALL_IPV6_HOST_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_TARBALL_IPV6_HOST_VAR_1
-->
${SLASH_COMMAND_PLUGIN_INSTALL_TARBALL_IPV6_HOST_VAR_0} cannot be used: it downloads from ${SLASH_COMMAND_PLUGIN_INSTALL_TARBALL_IPV6_HOST_VAR_1}, an IPv6 spelling of an IPv4 address, which your organization's plugin source rules cannot check. Ask whoever runs the registry to serve it from a hostname or an IPv4 address.
