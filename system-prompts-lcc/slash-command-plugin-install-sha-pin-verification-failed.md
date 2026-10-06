<!--
name: 'Plugin install: SHA pin verification failed'
description: >-
  Install failure when the checked-out commit does not match the entry's pinned
  sha.
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_SHA_PIN_VERIFICATION_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_SHA_PIN_VERIFICATION_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_SHA_PIN_VERIFICATION_FAILED_VAR_2
-->
SHA pin verification failed: expected ${SLASH_COMMAND_PLUGIN_INSTALL_SHA_PIN_VERIFICATION_FAILED_VAR_0} to be ${SLASH_COMMAND_PLUGIN_INSTALL_SHA_PIN_VERIFICATION_FAILED_VAR_1}, got ${SLASH_COMMAND_PLUGIN_INSTALL_SHA_PIN_VERIFICATION_FAILED_VAR_2||"(rev-parse failed)"}. The pinned commit may have been removed upstream, or a ref with the same name exists. Refusing to install.
