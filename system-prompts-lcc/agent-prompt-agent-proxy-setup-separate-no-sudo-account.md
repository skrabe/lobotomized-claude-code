<!--
name: 'Agent prompt: agent proxy setup separate no-sudo account'
description: >-
  Tells the session this is a separate account without sudo, root steps run by
  the admin, system unit required
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_SEPARATE_NO_SUDO_ACCOUNT_VAR_0
-->
The admin says this is a separate account with no sudo, ${AGENT_PROMPT_AGENT_PROXY_SETUP_SEPARATE_NO_SUDO_ACCOUNT_VAR_0.name}. Do not ask about a separate account again. The admin runs each step that needs root from their own login. The system unit is required here.
