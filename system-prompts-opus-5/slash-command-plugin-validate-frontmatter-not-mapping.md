<!--
name: 'Plugin validate: frontmatter is not a YAML mapping'
description: >-
  Error pushed by the /plugin validate frontmatter checker when the parsed YAML
  is not a key/value mapping.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_FRONTMATTER_NOT_MAPPING_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_FRONTMATTER_NOT_MAPPING_VAR_1
-->
Frontmatter must be a YAML mapping (key: value pairs), got ${SLASH_COMMAND_PLUGIN_VALIDATE_FRONTMATTER_NOT_MAPPING_VAR_0.isArray(SLASH_COMMAND_PLUGIN_VALIDATE_FRONTMATTER_NOT_MAPPING_VAR_1)?"an array":typeof SLASH_COMMAND_PLUGIN_VALIDATE_FRONTMATTER_NOT_MAPPING_VAR_1}.
