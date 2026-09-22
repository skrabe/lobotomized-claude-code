<!--
name: 'Data: Auto-Mode Classifier-Only No Prompt Raised'
description: >-
  Suffix interpolated into the classifierOnly deny tool_result when an ASK never
  raised a prompt and the classifier did not allow.
ccVersion: 2.1.265
variables:
  - DATA_AUTO_MODE_CLASSIFIER_ONLY_NO_PROMPT_RAISED_VAR_0
  - DATA_AUTO_MODE_CLASSIFIER_ONLY_NO_PROMPT_RAISED_VAR_1
-->
no prompt is raised for it, and the classifier did not allow it${DATA_AUTO_MODE_CLASSIFIER_ONLY_NO_PROMPT_RAISED_VAR_0.decisionReason?.DATA_AUTO_MODE_CLASSIFIER_ONLY_NO_PROMPT_RAISED_VAR_1==="other"?` (${DATA_AUTO_MODE_CLASSIFIER_ONLY_NO_PROMPT_RAISED_VAR_0.decisionReason.reason})`:""}
