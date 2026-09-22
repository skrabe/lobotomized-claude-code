<!--
name: Permission Classifier Host Always Block
description: >-
  Host-machine hard-deny rules section injected into the permission-classifier
  system prompt.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_PERMISSION_CLASSIFIER_HOST_ALWAYS_BLOCK_VAR_0
  - SYSTEM_PROMPT_PERMISSION_CLASSIFIER_HOST_ALWAYS_BLOCK_VAR_1
-->
Always block on that machine:
${SYSTEM_PROMPT_PERMISSION_CLASSIFIER_HOST_ALWAYS_BLOCK_VAR_0(SYSTEM_PROMPT_PERMISSION_CLASSIFIER_HOST_ALWAYS_BLOCK_VAR_1.hardDeny)}
