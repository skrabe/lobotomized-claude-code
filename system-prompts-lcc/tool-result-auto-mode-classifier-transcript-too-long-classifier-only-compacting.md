<!--
name: >-
  Tool Result: Auto Mode Classifier Transcript Too Long (classifier-only,
  compacting)
description: >-
  checkPermissions deny message when a classifierOnly tool was not reviewed
  because the conversation is too long for the auto-mode classifier, telling
  Claude the action did not run, is not judged unsafe, and to reissue it after
  compaction
ccVersion: 2.1.288
variables:
  - >-
    TOOL_RESULT_AUTO_MODE_CLASSIFIER_TRANSCRIPT_TOO_LONG_CLASSIFIER_ONLY_COMPACTING_VAR_0
-->
${TOOL_RESULT_AUTO_MODE_CLASSIFIER_TRANSCRIPT_TOO_LONG_CLASSIFIER_ONLY_COMPACTING_VAR_0.name} was not reviewed and did not run: the conversation is too long for auto mode's classifier, and no permission prompt is raised for this tool. This is not a judgment that the action is unsafe. Claude Code will try to compact the conversation before the next request; if this action is still needed after that, issue it again.
