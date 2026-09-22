<!--
name: 'Tool Result: Auto-Mode Classifier-Only Empty Input'
description: >-
  Deny tool_result when a classifierOnly tool serialized an empty
  toAutoClassifierInput, so only the classifier could allow it and nothing was
  judged.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_ONLY_EMPTY_INPUT_VAR_0
-->
${TOOL_RESULT_AUTO_MODE_CLASSIFIER_ONLY_EMPTY_INPUT_VAR_0.name} was not reviewed: it gave the auto mode classifier nothing to judge (its toAutoClassifierInput is empty), and only the classifier can allow it. This is a tool bug, not a judgment on the action.
