<!--
name: 'Agent Prompt: Narration Previous Line'
description: >-
  User-message template for the narration status-line model, including the
  previous status line.
ccVersion: 2.1.261
variables:
  - AGENT_PROMPT_NARRATION_PREVIOUS_LINE_VAR_0
  - AGENT_PROMPT_NARRATION_PREVIOUS_LINE_VAR_1
  - AGENT_PROMPT_NARRATION_PREVIOUS_LINE_VAR_2
-->
${AGENT_PROMPT_NARRATION_PREVIOUS_LINE_VAR_0}

${AGENT_PROMPT_NARRATION_PREVIOUS_LINE_VAR_1}

PREVIOUS LINE: ${AGENT_PROMPT_NARRATION_PREVIOUS_LINE_VAR_2??""}
