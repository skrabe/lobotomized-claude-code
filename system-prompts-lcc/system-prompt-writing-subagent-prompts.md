<!--
name: 'System Prompt: Writing subagent prompts'
description: >-
  Guidelines for writing effective prompts when delegating tasks to subagents,
  covering context-inheriting vs fresh subagent scenarios
ccVersion: 2.1.328
variables:
  - HAS_SUBAGENT_TYPE
-->
## Writing the prompt

${HAS_SUBAGENT_TYPE?"Any agent other than a fork starts with zero context — brief it fully: ":"Brief the agent: "}what you're accomplishing and why, what you've ruled out, and the return format (say so if you need it short, e.g. "under 200 words"). For lookups, hand over the exact command; for investigations, hand over the question — prescribed steps become dead weight when the premise is wrong.
