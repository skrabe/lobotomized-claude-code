<!--
name: 'Tool Result: Workshop verifier refuses non-SVG element inside SVG'
description: >-
  Hint in the workshop page structural-verifier refusal telling the model to
  remove an HTML element nested in SVG because browsers and the verifier parse
  what follows it differently
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_SVG_NON_SVG_ELEMENT_VAR_0
-->
Remove it — <${TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_SVG_NON_SVG_ELEMENT_VAR_0}> is not an SVG element, and browsers and this verifier parse what follows it differently, so later markup could go uninspected.
