<!--
name: 'Data: Skill Tool Spelling In Session'
description: >-
  Preamble injected into a skill telling the model this session's tool spelling
  and to load it on first use.
ccVersion: 2.1.257
variables:
  - DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_0
  - DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_1
  - DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_2
  - DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_3
-->
> Tool spelling in this session: ${DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_0.map((DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_1)=>DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_2[o]).join("; ")} — load it with ${DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_3} when you first need it. Read the steps below with that substitution.

