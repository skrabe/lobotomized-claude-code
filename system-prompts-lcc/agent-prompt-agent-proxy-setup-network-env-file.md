<!--
name: 'Agent prompt: agent proxy setup network environment file'
description: >-
  Tells the session to have the admin supply proxy network variable values into
  the EnvironmentFile and never copy them from the environment
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_0
  - AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_1
  - AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_2
  - AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_3
-->
This setup ran with ${AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_0.join(", ")} set, and the proxy needs the same: ask the admin for their values and put them in ${AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_1}, ${AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_2}, which the unit's EnvironmentFile= reads; if ${AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_3(AGENT_PROMPT_AGENT_PROXY_SETUP_NETWORK_ENV_FILE_VAR_1)} is not there, have the admin create it root:root 755 first. Never copy a value from this session's environment: a proxy address can carry a password.
