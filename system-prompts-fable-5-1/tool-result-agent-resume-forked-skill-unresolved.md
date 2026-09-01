<!--
name: 'Tool Result: Forked Skill No Longer Resolvable On Resume'
description: >-
  ResumeAgentStateError message refusing to resume an agent whose originating
  forked skill no longer resolves to a fork-capable skill, surfaced to the
  model in the SendMessage tool result.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_AGENT_RESUME_FORKED_SKILL_UNRESOLVED_VAR_0
  - TOOL_RESULT_AGENT_RESUME_FORKED_SKILL_UNRESOLVED_VAR_1
-->
Agent ${TOOL_RESULT_AGENT_RESUME_FORKED_SKILL_UNRESOLVED_VAR_0} ran as forked skill ${TOOL_RESULT_AGENT_RESUME_FORKED_SKILL_UNRESOLVED_VAR_1.skillName}, which no longer resolves to a fork-capable skill; refusing to resume it.
