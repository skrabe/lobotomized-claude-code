<!--
name: 'System Prompt: Artifact intake design system lookup via tool'
description: >-
  Design-system lookup step in artifact intake when the design-system search
  tool is available
ccVersion: 2.1.322
variables:
  - SYSTEM_PROMPT_ARTIFACT_INTAKE_DESIGN_SYSTEM_LOOKUP_TOOL_VAR_0
  - SYSTEM_PROMPT_ARTIFACT_INTAKE_DESIGN_SYSTEM_LOOKUP_TOOL_VAR_1
-->
call ${SYSTEM_PROMPT_ARTIFACT_INTAKE_DESIGN_SYSTEM_LOOKUP_TOOL_VAR_0(SYSTEM_PROMPT_ARTIFACT_INTAKE_DESIGN_SYSTEM_LOOKUP_TOOL_VAR_1)} once with type "Design System" and limit 3 and take the one marked default, or the first
