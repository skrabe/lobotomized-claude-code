<!--
name: 'Agent prompt: agent proxy setup restart as root without sudo'
description: >-
  Line telling the admin to restart the proxy unit with systemctl as root
  without sudo
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_NO_SUDO_RESTART_AS_ROOT_VAR_0
-->
  Then restart it, as root without sudo: systemctl restart ${AGENT_PROMPT_AGENT_PROXY_SETUP_NO_SUDO_RESTART_AS_ROOT_VAR_0}
