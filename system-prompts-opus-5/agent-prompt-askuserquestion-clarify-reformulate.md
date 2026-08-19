<!--
name: 'Agent Prompt: Clarify and reformulate questions'
description: >-
  prompt instructing the model to take the user's clarification into account and
  reformulate the questions
ccVersion: 2.1.235
variables:
  - AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_0
  - AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_1
  - AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_2
  - AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_3
  - AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_4
-->
The user wants to clarify these questions. Take their response into account and reformulate the questions if appropriate. Start by asking what they would like to clarify.

Questions asked:
${AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_0(AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_1,AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_2,AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_3,AGENT_PROMPT_ASKUSERQUESTION_CLARIFY_REFORMULATE_VAR_4.isScreenReader)}
