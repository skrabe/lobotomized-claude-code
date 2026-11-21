<!--
name: 'Tool result: app_type field left selected warning'
description: >-
  Tell the user (or say in result when unattended) the field may be left with
  all text selected.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_TYPE_FIELD_LEFT_SELECTED_WARNING_VAR_0
-->
${TOOL_RESULT_APP_TYPE_FIELD_LEFT_SELECTED_WARNING_VAR_0.isUnattended?"say in your result":"tell the user"} that this field may be left with all its text selected
