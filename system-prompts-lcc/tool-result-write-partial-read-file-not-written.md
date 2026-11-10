<!--
name: 'Tool Result: Write refused after partial read'
description: >-
  Write validation error when only the start of the file was read in this
  session, pointing to the edit tool and its link-target rule
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_WRITE_PARTIAL_READ_FILE_NOT_WRITTEN_VAR_0
-->
Only the start of this file was given in this session, so a Write could lose the rest. Nothing was written. To change it, use ${TOOL_RESULT_WRITE_PARTIAL_READ_FILE_NOT_WRITTEN_VAR_0}. If ${TOOL_RESULT_WRITE_PARTIAL_READ_FILE_NOT_WRITTEN_VAR_0} says that the path is a link, use it on the link's target.
