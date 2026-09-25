<!--
name: 'Tool result: git bundle attributes file remedy'
description: >-
  Remedy for core.attributesFile set outside the user's own config: move rules
  to .gitattributes or set it in user/system git config, then retry.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_ATTRIBUTES_FILE_REMEDY_VAR_0
-->
Move the attribute rules it points to into a .gitattributes file committed with the project, or set core.attributesFile directly in your user or system git config file to an absolute or ~/ path; then remove the setting from ${TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_ATTRIBUTES_FILE_REMEDY_VAR_0} and retry.
