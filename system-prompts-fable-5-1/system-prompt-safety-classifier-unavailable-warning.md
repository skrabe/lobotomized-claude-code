<!--
name: 'System Prompt: Safety Classifier Unavailable'
description: >-
  Warning injected into subagent output when the safety classifier was
  unavailable; asks the model to verify the subagent's actions.
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_0
  - SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_1
  - SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_2
  - SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_3
-->

Note: ${SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_0?`${SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_0} (the safety classifier)`:"The safety classifier"} was unavailable${SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_1(SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_2,SYSTEM_PROMPT_SAFETY_CLASSIFIER_UNAVAILABLE_WARNING_VAR_3)} when reviewing this subagent's work. Verify the subagent's actions and output before acting on them.
