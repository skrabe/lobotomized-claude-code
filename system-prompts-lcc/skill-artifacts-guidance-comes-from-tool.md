<!--
name: 'Skill: Artifacts guidance comes from a tool'
description: >-
  Body of the stand-in skill telling Claude that this session's guidance comes
  from an Artifacts MCP tool and when and how to call it.
ccVersion: 2.1.332
variables:
  - SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_0
  - SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_1
  - SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_2
  - SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_3
-->
In this session the ${SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_0.skill} guidance comes from a tool, not a skill. ${SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_0.when}, call \`${SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_1?.SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_2??SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_3(SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_0.tool)}\` ${SKILL_ARTIFACTS_GUIDANCE_COMES_FROM_TOOL_VAR_0.how}, and follow what it returns.
