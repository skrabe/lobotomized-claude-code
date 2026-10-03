<!--
name: 'Tool Result: Auto Mode Classifier Transcript Too Long (compacting)'
description: >-
  checkPermissions deny message when the auto-mode classifier transcript is too
  long and Claude Code will compact before the next request, telling Claude to
  reissue the action afterwards and it will be reviewed normally
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_TRANSCRIPT_TOO_LONG_COMPACTING_VAR_0
-->
${TOOL_RESULT_AUTO_MODE_CLASSIFIER_TRANSCRIPT_TOO_LONG_COMPACTING_VAR_0.name} was not reviewed and did not run: the conversation is too long for auto mode's classifier. Claude Code will try to compact the conversation before the next request; if this action is still needed after that, issue it again and it will be reviewed normally.
