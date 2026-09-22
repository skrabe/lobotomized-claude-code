<!--
name: 'Tool Result: Artifact Publish Contract Echo Rejected'
description: >-
  Publish error when the service refuses a stored contract pin, steering a retry
  with contract latest or a user-facing explanation.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_CONTRACT_PIN_YANKED_VAR_0
-->
contract pin (${TOOL_RESULT_ARTIFACT_CONTRACT_PIN_YANKED_VAR_0.pin}) and nothing was published. If the reason above says the pin was yanked, pass contract: 'latest' to move the artifact to the current contract (this changes the page's runtime semantics); otherwise tell the user what the service said.
