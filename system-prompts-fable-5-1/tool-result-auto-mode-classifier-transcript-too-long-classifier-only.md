<!--
name: 'Tool Result: Auto Mode Classifier Transcript Too Long (classifier-only)'
description: >-
  checkPermissions deny message when a classifierOnly tool cannot be reviewed
  because the auto-mode classifier transcript exceeded its context window and no
  permission prompt is raised.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_TRANSCRIPT_TOO_LONG_CLASSIFIER_ONLY_VAR_0
-->
${TOOL_RESULT_AUTO_MODE_CLASSIFIER_TRANSCRIPT_TOO_LONG_CLASSIFIER_ONLY_VAR_0.name} was not reviewed: the auto mode classifier transcript exceeded its context window, and no permission prompt is raised for this tool. This is not a judgment that the action is unsafe; the same call will hit the same limit until the conversation is shorter.
