<!--
name: 'Skill: Code Review Single-Pass Disclosure'
description: >-
  Fragment appended to the code-review skill prompt when the Agent tool is
  unavailable, telling the model to disclose that only a single-pass review ran.
ccVersion: 2.1.214
variables:
  - SKILL_CODE_REVIEW_SINGLE_PASS_DISCLOSURE_VAR_0
-->


State in your summary that this was a single-pass review done without the
${SKILL_CODE_REVIEW_SINGLE_PASS_DISCLOSURE_VAR_0} tool, not the full multi-agent fan-out.
