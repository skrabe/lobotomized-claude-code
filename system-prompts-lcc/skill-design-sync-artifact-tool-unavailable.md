<!--
name: 'Skill: Design-sync artifact tool unavailable'
description: >-
  Reason that the artifact tool is missing from the session, listing the usual
  conditions for it to be available.
ccVersion: 2.1.330
variables:
  - SKILL_DESIGN_SYNC_ARTIFACT_TOOL_UNAVAILABLE_VAR_0
-->
The ${SKILL_DESIGN_SYNC_ARTIFACT_TOOL_UNAVAILABLE_VAR_0} tool, which /design-sync publishes with, is not available in this session. As a rule it is available in a session on the user's own machine that is signed in with claude.ai on a paid plan, has Artifacts on in /config, has no /permissions rule that denies the tool, and whose organization allows artifacts. Once that holds, they can start a new session and run /design-sync again; if it all holds already, the cause is a rarer one that this list leaves out.
