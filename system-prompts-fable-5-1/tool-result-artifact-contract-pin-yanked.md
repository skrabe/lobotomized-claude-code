<!--
name: Artifact contract-pin error
description: >-
  Republish error returned to the model explaining the echoed contract pin and
  how to move to latest or fix the declaration.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_ARTIFACT_CONTRACT_PIN_YANKED_VAR_0
-->
contract pin (${TOOL_RESULT_ARTIFACT_CONTRACT_PIN_YANKED_VAR_0.pin}). If the reason above says the pin was yanked, pass contract: 'latest' to move the artifact to the current contract (this changes the page's runtime semantics). If the reason concerns the capability declaration 
