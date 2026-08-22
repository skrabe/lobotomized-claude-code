<!--
name: Agent proxy preconfigured-CLIs env note
description: >-
  Clause appended to the agent-proxy environment note listing the CLIs already
  configured for the proxy and telling the model to prefer a skill/MCP tool,
  then those CLIs, over raw curl.
ccVersion: 2.1.239
variables:
  - SYSTEM_PROMPT_AGENT_PROXY_PRECONFIGURED_CLIS_NOTE_VAR_0
-->
 Installed CLIs preconfigured for the proxy: ${SYSTEM_PROMPT_AGENT_PROXY_PRECONFIGURED_CLIS_NOTE_VAR_0.join(", ")} — 
