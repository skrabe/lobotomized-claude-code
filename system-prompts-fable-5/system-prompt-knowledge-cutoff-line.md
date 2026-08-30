<!--
name: Knowledge Cutoff Line
description: >-
  Model-facing 'Assistant knowledge cutoff is ${date}.' line emitted in the
  environment system-prompt blocks (b2m/S2m/T2m); conditional on a known cutoff
  for the model.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_KNOWLEDGE_CUTOFF_LINE_VAR_0
-->
Assistant knowledge cutoff is ${SYSTEM_PROMPT_KNOWLEDGE_CUTOFF_LINE_VAR_0.knowledgeCutoff}.
