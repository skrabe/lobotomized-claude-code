<!--
name: Eval criterion grader — intro
description: >-
  Opening line of the LLM-grader prompt that judges a coding-agent's output
  against a criterion during `plugin eval`.
ccVersion: 2.1.234
variables:
  - AGENT_PROMPT_EVAL_CRITERION_GRADER_VAR_0
-->
You are grading the output of a coding agent against a criterion.

Criterion:
${AGENT_PROMPT_EVAL_CRITERION_GRADER_VAR_0.criteria}
