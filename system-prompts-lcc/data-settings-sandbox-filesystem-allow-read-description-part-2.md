<!--
name: 'Data: sandbox.filesystem.allowRead setting description (part 2 of 2)'
description: >-
  Description of the `sandbox.filesystem.allowRead` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.285
variables:
  - DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_READ_DESCRIPTION_PART_2_VAR_0
  - DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_READ_DESCRIPTION_PART_2_VAR_1
-->
${DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_READ_DESCRIPTION_PART_2_VAR_0}, a value from ${DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_READ_DESCRIPTION_PART_2_VAR_1} that would re-open a path managed, --settings or user settings deny reading is ignored, as is one spelled as a glob or a network path (UNC or automount); one carving out of the project's own denyRead still applies. A value inside a directory sandboxed commands can write is re-checked before every command and dropped once it has been re-pointed into a denied path.
