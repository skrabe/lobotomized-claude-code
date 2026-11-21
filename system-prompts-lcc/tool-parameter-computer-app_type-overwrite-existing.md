<!--
name: 'Tool Parameter: Computer app_type overwrite_existing'
description: >-
  overwrite_existing parameter: when needed and that it may replace all field
  content
ccVersion: 2.1.330
variables:
  - TOOL_PARAMETER_COMPUTER_APP_TYPE_OVERWRITE_EXISTING_VAR_0
-->
doesn't work for this app and the field already has content, where the only background fallback is replacing the WHOLE field. A selection or content whose read fails, or that the app counts but does not show, counts as being there. Set true to proceed. In either case this can replace ALL of the field's content; ${TOOL_PARAMETER_COMPUTER_APP_TYPE_OVERWRITE_EXISTING_VAR_0}, so a longer text cannot be restored from the result.
