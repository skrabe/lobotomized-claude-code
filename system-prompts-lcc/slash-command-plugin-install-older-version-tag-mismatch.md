<!--
name: '/plugin install: older version does not match its tag'
description: >-
  Install refusal when the requested older version's checkout does not match its
  tag or package; the reason is appended.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_OLDER_VERSION_TAG_MISMATCH_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_OLDER_VERSION_TAG_MISMATCH_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_OLDER_VERSION_TAG_MISMATCH_VAR_2
-->
"${SLASH_COMMAND_PLUGIN_INSTALL_OLDER_VERSION_TAG_MISMATCH_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_OLDER_VERSION_TAG_MISMATCH_VAR_1.name,120)}" was not installed at that version: ${SLASH_COMMAND_PLUGIN_INSTALL_OLDER_VERSION_TAG_MISMATCH_VAR_2}.
