<!--
name: 'System Prompt: Auto-Mode Classifier Remote Machine Allow'
description: >-
  Allow-exception list from the remote host, interpolated into the auto-mode
  classifier prompt so those ALLOW rules can clear a SOFT BLOCK.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_AUTO_MODE_CLASSIFIER_REMOTE_MACHINE_ALLOW_VAR_0
  - SYSTEM_PROMPT_AUTO_MODE_CLASSIFIER_REMOTE_MACHINE_ALLOW_VAR_1
-->
Allowed on that machine (exceptions its user explicitly permits there — apply each as you apply the ALLOW exceptions above: it can clear a SOFT BLOCK rule or a "Block … unless" line here, never a HARD BLOCK or an "Always block" line):
${SYSTEM_PROMPT_AUTO_MODE_CLASSIFIER_REMOTE_MACHINE_ALLOW_VAR_0(SYSTEM_PROMPT_AUTO_MODE_CLASSIFIER_REMOTE_MACHINE_ALLOW_VAR_1.allow)}
