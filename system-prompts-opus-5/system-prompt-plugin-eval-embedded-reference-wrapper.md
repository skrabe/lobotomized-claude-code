<!--
name: 'System Prompt: Plugin eval embedded offline reference wrapper'
description: >-
  Wrapper block that heads the embedded offline reference in the claude-code
  docs skill prompt, stating the current session's plugin eval and /skill-doctor
  status before the quick-reference body
ccVersion: 2.1.233
variables:
  - SYSTEM_PROMPT_PLUGIN_EVAL_EMBEDDED_REFERENCE_WRAPPER_VAR_0
  - SYSTEM_PROMPT_PLUGIN_EVAL_EMBEDDED_REFERENCE_WRAPPER_VAR_1
  - SYSTEM_PROMPT_PLUGIN_EVAL_EMBEDDED_REFERENCE_WRAPPER_VAR_2
-->
# Plugin eval and /skill-doctor (embedded offline reference)

In THIS session: ${SYSTEM_PROMPT_PLUGIN_EVAL_EMBEDDED_REFERENCE_WRAPPER_VAR_0.text} ${SYSTEM_PROMPT_PLUGIN_EVAL_EMBEDDED_REFERENCE_WRAPPER_VAR_1}

${SYSTEM_PROMPT_PLUGIN_EVAL_EMBEDDED_REFERENCE_WRAPPER_VAR_2}
