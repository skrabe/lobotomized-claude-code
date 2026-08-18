<!--
name: 'System prompt: System reminder framing tag'
description: >-
  The wrapper template that encloses injected reminder content in
  <\system-reminder> tags before it reaches the model
ccVersion: 2.1.234
variables:
  - SYSTEM_PROMPT_SYSTEM_REMINDER_FRAMING_TAG_VAR_0
  - SYSTEM_PROMPT_SYSTEM_REMINDER_FRAMING_TAG_VAR_1
  - SYSTEM_PROMPT_SYSTEM_REMINDER_FRAMING_TAG_VAR_2
-->
<system-reminder>
${SYSTEM_PROMPT_SYSTEM_REMINDER_FRAMING_TAG_VAR_0(SYSTEM_PROMPT_SYSTEM_REMINDER_FRAMING_TAG_VAR_1)}${SYSTEM_PROMPT_SYSTEM_REMINDER_FRAMING_TAG_VAR_2}
