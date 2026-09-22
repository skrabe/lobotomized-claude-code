<!--
name: 'Tool Description: Invoke Skill (Coordinator Read-Only)'
description: >-
  Coordinator-session addendum to the Skill tool description: the coordinator
  loads instructions read-only and must hand execution to workers.
ccVersion: 2.1.238
variables:
  - TOOL_DESCRIPTION_INVOKE_SKILL_COORDINATOR_READONLY_VAR_0
-->

Worker skill invocations execute normally. A \`<${TOOL_DESCRIPTION_INVOKE_SKILL_COORDINATOR_READONLY_VAR_0}>\` block that arrived with only a delegation summary (no skill content) does not mean the skill is loaded — calling this tool to load it is still appropriate then.
