<!--
name: '/plugin install: copy source directory is a link'
description: >-
  Copy refusal when a listed directory in the plugin source turned into a link
  or junction.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_COPY_DIRECTORY_BECAME_LINK_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_COPY_DIRECTORY_BECAME_LINK_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_COPY_DIRECTORY_BECAME_LINK_VAR_2
-->
Refusing to copy ${SLASH_COMMAND_PLUGIN_INSTALL_COPY_DIRECTORY_BECAME_LINK_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_COPY_DIRECTORY_BECAME_LINK_VAR_1,SLASH_COMMAND_PLUGIN_INSTALL_COPY_DIRECTORY_BECAME_LINK_VAR_2.name)}: it is no longer a directory as listed — a link or Windows junction stands there (planted, or swapped during the copy). Plugin trees must hold plain directories.
