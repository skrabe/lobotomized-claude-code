<!--
name: 'Tool Result: Read path leads through /proc or /dev link'
description: >-
  Validation error that a path is or leads through a /proc or /dev link the tool
  does not follow
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_READ_PATH_LEADS_THROUGH_PROC_DEV_LINK_VAR_0
  - TOOL_RESULT_READ_PATH_LEADS_THROUGH_PROC_DEV_LINK_VAR_1
  - TOOL_RESULT_READ_PATH_LEADS_THROUGH_PROC_DEV_LINK_VAR_2
-->
Cannot read '${TOOL_RESULT_READ_PATH_LEADS_THROUGH_PROC_DEV_LINK_VAR_0(TOOL_RESULT_READ_PATH_LEADS_THROUGH_PROC_DEV_LINK_VAR_1)}': it is or leads to ${TOOL_RESULT_READ_PATH_LEADS_THROUGH_PROC_DEV_LINK_VAR_2}.
