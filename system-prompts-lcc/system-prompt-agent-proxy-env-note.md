<!--
name: Agent Proxy Environment Note
description: >-
  Concise agent-proxy/TLS guidance stored via rDt and injected into the <env>
  'useful information about the environment' context block the model reads.
ccVersion: 2.1.330
variables:
  - SYSTEM_PROMPT_AGENT_PROXY_ENV_NOTE_VAR_0
  - SYSTEM_PROMPT_AGENT_PROXY_ENV_NOTE_VAR_1
  - SYSTEM_PROMPT_AGENT_PROXY_ENV_NOTE_VAR_2
-->
Outbound HTTPS goes through a pre-configured agent proxy (CA bundle: ${SYSTEM_PROMPT_AGENT_PROXY_ENV_NOTE_VAR_0}). If a tool fails TLS verification, gets 403/405/407 from the proxy, or a transfer is cut off (connection reset, unexpected disconnect, RPC failed), ${SYSTEM_PROMPT_AGENT_PROXY_ENV_NOTE_VAR_1}; never disable TLS verification or unset HTTPS_PROXY. When the proxy refused or lost a connection during a ${SYSTEM_PROMPT_AGENT_PROXY_ENV_NOTE_VAR_2} command that failed in the foreground, [agent-proxy] lines at the end of its output say which host and why.
