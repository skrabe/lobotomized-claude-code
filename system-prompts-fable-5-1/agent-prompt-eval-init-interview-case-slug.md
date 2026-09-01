<!--
name: 'Eval-authoring interview: user-suggested case slug'
description: >-
  Optional clause in the `claude plugin eval init` interview system prompt
  telling the model to use the case slug the user suggested where it fits.
ccVersion: 2.1.235
variables:
  - AGENT_PROMPT_EVAL_INIT_INTERVIEW_CASE_SLUG_VAR_0
  - AGENT_PROMPT_EVAL_INIT_INTERVIEW_CASE_SLUG_VAR_1
  - AGENT_PROMPT_EVAL_INIT_INTERVIEW_CASE_SLUG_VAR_2
-->
 The user suggested ${AGENT_PROMPT_EVAL_INIT_INTERVIEW_CASE_SLUG_VAR_0(AGENT_PROMPT_EVAL_INIT_INTERVIEW_CASE_SLUG_VAR_1.stringify(AGENT_PROMPT_EVAL_INIT_INTERVIEW_CASE_SLUG_VAR_2))} as a case slug; use it where it fits.
