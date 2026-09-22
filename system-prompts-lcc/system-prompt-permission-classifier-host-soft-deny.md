<!--
name: Permission Classifier Host Soft Deny
description: >-
  Host-machine soft-deny rules section injected into the permission-classifier
  system prompt.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_PERMISSION_CLASSIFIER_HOST_SOFT_DENY_VAR_0
  - SYSTEM_PROMPT_PERMISSION_CLASSIFIER_HOST_SOFT_DENY_VAR_1
-->
Block on that machine unless the user clearly asked for exactly this:
${SYSTEM_PROMPT_PERMISSION_CLASSIFIER_HOST_SOFT_DENY_VAR_0(SYSTEM_PROMPT_PERMISSION_CLASSIFIER_HOST_SOFT_DENY_VAR_1.softDeny)}
