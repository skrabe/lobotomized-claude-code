<!--
name: 'Tool result: git bundle config location remedy'
description: >-
  Remedy telling the user to set HOME (or the named variable) to a full path and
  restart Claude Code.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_CONFIG_LOCATION_REMEDY_VAR_0
-->
Set ${TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_CONFIG_LOCATION_REMEDY_VAR_0==="HOMEPATH"||TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_CONFIG_LOCATION_REMEDY_VAR_0==="USERPROFILE"?"HOME":TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_CONFIG_LOCATION_REMEDY_VAR_0} to a full path (on Windows, one that starts with a drive letter), then start Claude Code again.
