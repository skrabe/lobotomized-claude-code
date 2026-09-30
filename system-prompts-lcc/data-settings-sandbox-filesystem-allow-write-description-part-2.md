<!--
name: 'Data: sandbox.filesystem.allowWrite setting description (part 2 of 2)'
description: >-
  Description of the `sandbox.filesystem.allowWrite` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.285
variables:
  - DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_WRITE_DESCRIPTION_PART_2_VAR_0
  - DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_WRITE_DESCRIPTION_PART_2_VAR_1
  - DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_WRITE_DESCRIPTION_PART_2_VAR_2
-->
${DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_WRITE_DESCRIPTION_PART_2_VAR_0} ${DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_WRITE_DESCRIPTION_PART_2_VAR_1}, a value from ${DATA_SETTINGS_SANDBOX_FILESYSTEM_ALLOW_WRITE_DESCRIPTION_PART_2_VAR_2} under or equal to a denied path, or spelled as a glob or a network path (UNC or automount), is ignored. A value inside a directory sandboxed commands can already write is re-checked before every command and dropped once it has been re-pointed into a denied read path.
