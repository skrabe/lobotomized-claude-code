<!--
name: 'Agent prompt: agent proxy setup user-unit env file ownership'
description: >-
  Ownership note for the network environment file in a user unit, owned by the
  login account at 600
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_USER_UNIT_ENV_FILE_OWNER_VAR_0
-->
owned by ${AGENT_PROMPT_AGENT_PROXY_SETUP_USER_UNIT_ENV_FILE_OWNER_VAR_0.name} at 600, since the user manager reads it as ${AGENT_PROMPT_AGENT_PROXY_SETUP_USER_UNIT_ENV_FILE_OWNER_VAR_0.name}
