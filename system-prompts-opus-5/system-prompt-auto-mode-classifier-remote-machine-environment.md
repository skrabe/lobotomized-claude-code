<!--
name: 'System Prompt: Auto-Mode Classifier Remote Machine Environment'
description: >-
  Environment lines from the remote host, interpolated into the auto-mode
  classifier prompt as context for judging the command.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_AUTO_MODE_CLASSIFIER_REMOTE_MACHINE_ENVIRONMENT_VAR_0
  - SYSTEM_PROMPT_AUTO_MODE_CLASSIFIER_REMOTE_MACHINE_ENVIRONMENT_VAR_1
-->
About that machine (context for judging the command):
${SYSTEM_PROMPT_AUTO_MODE_CLASSIFIER_REMOTE_MACHINE_ENVIRONMENT_VAR_0(SYSTEM_PROMPT_AUTO_MODE_CLASSIFIER_REMOTE_MACHINE_ENVIRONMENT_VAR_1.environment)}
