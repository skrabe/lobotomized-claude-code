<!--
name: Output Style System-Prompt Header
description: >-
  Model-facing system-prompt block (s2m) framing a custom output style's prompt
  ("# Output Style: ${name}\n${prompt}"); conditional on a non-default output
  style being active.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_OUTPUT_STYLE_FRAMING_HEADER_VAR_0
-->
# Output Style: ${SYSTEM_PROMPT_OUTPUT_STYLE_FRAMING_HEADER_VAR_0}
${SYSTEM_PROMPT_OUTPUT_STYLE_FRAMING_HEADER_VAR_1}
