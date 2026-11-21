<!--
name: 'Skill: Design-sync design-system artifacts switched off'
description: >-
  Reason that the artifact tool cannot publish a Design System artifact, naming
  the account rollout or the env vars that turn it off.
ccVersion: 2.1.330
variables:
  - SKILL_DESIGN_SYNC_ARTIFACT_TYPE_SWITCHED_OFF_VAR_0
-->
The ${SKILL_DESIGN_SYNC_ARTIFACT_TYPE_SWITCHED_OFF_VAR_0} tool is in this session, but it can't publish to a Design System artifact, and starting a new session won't change that. There are two likely causes: Design System artifacts aren't switched on for their account yet, or their environment sets CLAUDE_CODE_ARTIFACT_MULTI_FILE, CLAUDE_CODE_ARTIFACT_TYPES or CLAUDE_CODE_ARTIFACT_TYPE_CATALOG to 0. If you can tell which applies, say so.
