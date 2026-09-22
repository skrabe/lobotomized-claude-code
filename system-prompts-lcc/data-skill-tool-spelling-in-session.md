<!--
name: 'Data: Skill Tool Spelling In Session'
description: >-
  Preamble injected into a skill telling the model this session's tool spelling
  and to load it on first use.
ccVersion: 2.1.259
variables:
  - DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_0
  - DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_1
  - DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_2
  - DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_3
-->
> Tool spelling in this session: ${DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_0.map(DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_1).join("; ")} — load it with ${DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_2} when you first need it. ${DATA_SKILL_TOOL_SPELLING_IN_SESSION_VAR_3}

