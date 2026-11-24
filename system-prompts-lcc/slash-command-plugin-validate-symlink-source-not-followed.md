<!--
name: 'Plugin validate: symlinked source not followed'
description: >-
  Validation message tail explaining validation doesn't follow symlinks while
  install dereferences them.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_SOURCE_NOT_FOLLOWED_VAR_0
-->
validation never follows one. Install dereferences symlinks that stay inside the marketplace, so this entry still loads${SLASH_COMMAND_PLUGIN_VALIDATE_SYMLINK_SOURCE_NOT_FOLLOWED_VAR_0()?", unless it leads into a .git folder":""}. Validate the real path separately.
