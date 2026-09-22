<!--
name: 'Skill: Code Review Without Task Tool (Single Pass)'
description: >-
  Code-review skill prompt fragment substituted when the Task tool is
  unavailable, instructing the model to work every angle in one pass instead of
  fanning out.
ccVersion: 2.1.214
variables:
  - SKILL_CODE_REVIEW_NO_TASK_TOOL_SINGLE_PASS_VAR_0
-->
The ${SKILL_CODE_REVIEW_NO_TASK_TOOL_SINGLE_PASS_VAR_0} tool isn't available in this context, so the usual
multi-agent fan-out and subagent verify pass can't run. Work through every
angle below yourself, in this same context, in one pass. Re-check each
candidate against the diff before keeping it; drop anything you can't back up
with a concrete failure scenario.
