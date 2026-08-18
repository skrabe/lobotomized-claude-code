<!--
name: Plugin eval LLM grader agent-output prompt
description: >-
  Text-focus body of the plugin-eval LLM grader prompt: wraps the criterion
  header, the (elision-truncated) agent output for the focus, and the one-word
  PASS/FAIL response instruction.
ccVersion: 2.1.234
variables:
  - AGENT_PROMPT_EVAL_LLM_GRADER_AGENT_OUTPUT_VAR_0
  - AGENT_PROMPT_EVAL_LLM_GRADER_AGENT_OUTPUT_VAR_1
  - AGENT_PROMPT_EVAL_LLM_GRADER_AGENT_OUTPUT_VAR_2
  - AGENT_PROMPT_EVAL_LLM_GRADER_AGENT_OUTPUT_VAR_3
-->
${AGENT_PROMPT_EVAL_LLM_GRADER_AGENT_OUTPUT_VAR_0}


Agent output (${AGENT_PROMPT_EVAL_LLM_GRADER_AGENT_OUTPUT_VAR_1(AGENT_PROMPT_EVAL_LLM_GRADER_AGENT_OUTPUT_VAR_2.focus)}):
${AGENT_PROMPT_EVAL_LLM_GRADER_AGENT_OUTPUT_VAR_3}


Respond with exactly one word: PASS or FAIL.
