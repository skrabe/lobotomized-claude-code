<!--
name: 'Tool Result: Outside Read Declined With Feedback'
description: >-
  checkPermissions ask message when the user declines an
  outside-working-directory read and leaves feedback; becomes the tool_result if
  they do not allow it.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_PERMISSION_OUTSIDE_READ_DECLINED_WITH_FEEDBACK_VAR_0
-->
The user did not allow this read outside the working directories: ${TOOL_RESULT_PERMISSION_OUTSIDE_READ_DECLINED_WITH_FEEDBACK_VAR_0.feedback}
