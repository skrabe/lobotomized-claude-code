<!--
name: 'Agent prompt: Eval judge image focus intro'
description: >-
  Prefix of the eval judge's user message when the graded agent output is an
  attached image rather than text
ccVersion: 2.1.234
variables:
  - AGENT_PROMPT_EVAL_JUDGE_IMAGE_FOCUS_INTRO_VAR_0
  - AGENT_PROMPT_EVAL_JUDGE_IMAGE_FOCUS_INTRO_VAR_1
  - AGENT_PROMPT_EVAL_JUDGE_IMAGE_FOCUS_INTRO_VAR_2
-->
${AGENT_PROMPT_EVAL_JUDGE_IMAGE_FOCUS_INTRO_VAR_0}

Agent output (${AGENT_PROMPT_EVAL_JUDGE_IMAGE_FOCUS_INTRO_VAR_1(AGENT_PROMPT_EVAL_JUDGE_IMAGE_FOCUS_INTRO_VAR_2.focus)}) is the attached image:
