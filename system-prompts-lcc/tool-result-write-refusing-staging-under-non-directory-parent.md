<!--
name: 'Tool result: write refused, staging dir parent is not a directory'
description: >-
  Error returned when an atomic write's staging directory sits under a symlinked
  or non-directory parent and the write is refused.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_REFUSING_STAGING_UNDER_NON_DIRECTORY_PARENT_VAR_0
  - TOOL_RESULT_WRITE_REFUSING_STAGING_UNDER_NON_DIRECTORY_PARENT_VAR_1
-->
Refusing to stage atomic write under non-directory parent: ${TOOL_RESULT_WRITE_REFUSING_STAGING_UNDER_NON_DIRECTORY_PARENT_VAR_0(TOOL_RESULT_WRITE_REFUSING_STAGING_UNDER_NON_DIRECTORY_PARENT_VAR_1)}
