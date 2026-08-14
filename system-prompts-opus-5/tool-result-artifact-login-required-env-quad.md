<!--
name: 'Tool Result: Artifact login required (federation env quad)'
description: >-
  Artifact tool error returned to the model when API access comes from managed
  settings or the ANTHROPIC_FEDERATION_RULE_ID / ANTHROPIC_ORGANIZATION_ID
  variables and a claude.ai login is still needed.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_ARTIFACT_LOGIN_REQUIRED_ENV_QUAD_VAR_0
-->
Artifacts need a claude.ai login. This session's API access is set up by ${TOOL_RESULT_ARTIFACT_LOGIN_REQUIRED_ENV_QUAD_VAR_0?"your organization's managed settings":"the ANTHROPIC_FEDERATION_RULE_ID / ANTHROPIC_ORGANIZATION_ID environment variables"}, which stays active for everything else — artifacts also use a claude.ai account. Run /login and select "Claude account with subscription", then retry.
