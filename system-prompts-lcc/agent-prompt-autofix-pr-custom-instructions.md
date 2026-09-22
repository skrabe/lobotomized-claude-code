<!--
name: 'Autofix PR agent: custom-instructions note'
description: >-
  Sentence appended to the cloud autofix-PR agent's initial monitoring prompt
  pointing it at custom autofix instruction files.
ccVersion: 2.1.206
variables:
  - AGENT_PROMPT_AUTOFIX_PR_CUSTOM_INSTRUCTIONS_VAR_0
-->
 Run ${AGENT_PROMPT_AUTOFIX_PR_CUSTOM_INSTRUCTIONS_VAR_0.join(" and ")} for custom instructions on how to autofix.
