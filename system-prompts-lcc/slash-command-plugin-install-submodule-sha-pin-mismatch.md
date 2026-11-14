<!--
name: '/plugin install: submodule SHA pin mismatch'
description: >-
  Install refusal when a cloned plugin's submodule is checked out at a different
  commit than its parent repository records; asks the user to have the
  maintainer fix the submodule.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_2
  - SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_3
  - SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_4
-->
SHA pin verification failed: submodule ${SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_1+SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_2)} is on commit ${SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_3}, but its parent repository records ${SLASH_COMMAND_PLUGIN_INSTALL_SUBMODULE_SHA_PIN_MISMATCH_VAR_4}. The submodule's remote may have removed the recorded commit, or have a branch named after it. Refusing to use this repository; ask the repository's maintainer to fix the submodule.
