<!--
name: 'Tool Result: Auto mode classifier transcript too long'
description: >-
  Deny message when auto mode's classifier cannot review an action because the
  conversation is too long
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_AUTO_MODE_CLASSIFIER_TRANSCRIPT_TOO_LONG_VAR_0
-->
${TOOL_RESULT_AUTO_MODE_CLASSIFIER_TRANSCRIPT_TOO_LONG_VAR_0.name} was not reviewed and did not run: the conversation is too long for auto mode's classifier. This is not a judgment that the action is unsafe; it cannot be reviewed until the conversation is shorter.
