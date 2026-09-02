<!--
name: 'System Prompt: Memory type privacy defaults'
description: >-
  Parameterized memory system-prompt line stating which memory types default to
  private vs. the shared/team destination.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_TYPE_PRIVACY_DEFAULTS_VAR_0
-->
\`user\` memories are always private; default \`feedback\` to private, \`project\` and \`reference\` to ${SYSTEM_PROMPT_MEMORY_TYPE_PRIVACY_DEFAULTS_VAR_0}.
