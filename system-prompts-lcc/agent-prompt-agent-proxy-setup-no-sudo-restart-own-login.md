<!--
name: 'Agent prompt: agent proxy setup restart from own login'
description: >-
  Line telling the admin to restart the proxy unit via sudo systemctl from their
  own login
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_NO_SUDO_RESTART_OWN_LOGIN_VAR_0
-->
  Then restart it, from your own login: sudo systemctl restart ${AGENT_PROMPT_AGENT_PROXY_SETUP_NO_SUDO_RESTART_OWN_LOGIN_VAR_0}
