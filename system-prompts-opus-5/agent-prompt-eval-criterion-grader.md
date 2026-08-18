<!--
name: 'Agent Prompt: Eval criterion grader'
description: >-
  Judge prompt asking the model to grade a coding agent's output against a
  stated criterion
ccVersion: 2.1.234
variables:
  - AGENT_PROMPT_EVAL_CRITERION_GRADER_VAR_0
-->
You are grading the output of a coding agent against a criterion.

Criterion:
${AGENT_PROMPT_EVAL_CRITERION_GRADER_VAR_0.criteria}
