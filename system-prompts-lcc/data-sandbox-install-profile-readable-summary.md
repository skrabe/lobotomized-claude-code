<!--
name: 'Data: Sandbox install profile readable summary'
description: >-
  Summarizes which profile tool directories sandboxed commands can now read,
  including package-manager configuration that may hold tokens
ccVersion: 2.1.325
variables:
  - DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_0
  - DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_1
  - DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_2
  - DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_3
  - DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_4
  - DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_5
  - DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_6
-->
 Sandboxed commands can now read the tool directories of your user profile (${DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_0}), including package-manager configuration that can hold feed tokens (.npmrc, pip.ini, NuGet.Config, Maven settings.xml, gradle.properties, .gitconfig): ${DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_1} folders made readable, ${DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_2} excluded${DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_3.length>0?`, ${DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_3.length} left unreadable because their permissions could not be changed`:""}. ${DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_4} ${DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_5} ${DATA_SANDBOX_INSTALL_PROFILE_READABLE_SUMMARY_VAR_6()}
