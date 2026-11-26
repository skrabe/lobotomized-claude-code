<!--
name: 'Agent prompt: agent proxy setup hosts to keep allowed'
description: Lists the update download host and Anthropic API host that must stay allowed
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_HOSTS_TO_KEEP_ALLOWED_VAR_0
  - AGENT_PROMPT_AGENT_PROXY_SETUP_HOSTS_TO_KEEP_ALLOWED_VAR_1
  - AGENT_PROMPT_AGENT_PROXY_SETUP_HOSTS_TO_KEEP_ALLOWED_VAR_2
-->
Hosts to keep allowed: ${new AGENT_PROMPT_AGENT_PROXY_SETUP_HOSTS_TO_KEEP_ALLOWED_VAR_0(AGENT_PROMPT_AGENT_PROXY_SETUP_HOSTS_TO_KEEP_ALLOWED_VAR_1).host}, where \`claude update\` downloads from, and the Anthropic API (${new AGENT_PROMPT_AGENT_PROXY_SETUP_HOSTS_TO_KEEP_ALLOWED_VAR_0(AGENT_PROMPT_AGENT_PROXY_SETUP_HOSTS_TO_KEEP_ALLOWED_VAR_2).host}).
