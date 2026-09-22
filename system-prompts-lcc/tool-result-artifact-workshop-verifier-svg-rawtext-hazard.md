<!--
name: 'Workshop Verifier: SVG Rawtext Hazard'
description: >-
  Verifier violation hint returned when a rawtext-named element appears inside
  an SVG subtree.
ccVersion: 2.1.219
variables:
  - TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_SVG_RAWTEXT_HAZARD_VAR_0
-->
Remove it — <${TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_SVG_RAWTEXT_HAZARD_VAR_0}> inside SVG is a serialization-hazard surface (mutation-XSS carrier); SVG diagrams need none of the rawtext-named elements.
