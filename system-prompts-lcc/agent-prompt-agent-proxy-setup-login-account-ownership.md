<!--
name: 'Agent prompt: agent proxy setup login account and file ownership'
description: >-
  Specifies the proxy login account, no service user/group, and owners/modes for
  folders, keys, secrets, hooks and logs
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_LOGIN_ACCOUNT_OWNERSHIP_VAR_0
  - AGENT_PROMPT_AGENT_PROXY_SETUP_LOGIN_ACCOUNT_OWNERSHIP_VAR_1
-->
Login account (the proxy's user): ${AGENT_PROMPT_AGENT_PROXY_SETUP_LOGIN_ACCOUNT_OWNERSHIP_VAR_0.name}, in its own primary group; the unit sets no Group=. Create no service user or group: this session creates none. Folders, /etc/agent-proxy and the secrets folders included, are root:root 755. Owned by ${AGENT_PROMPT_AGENT_PROXY_SETUP_LOGIN_ACCOUNT_OWNERSHIP_VAR_0.name} at 600: the key, the interception CA key, the TLS key, each secret's file, named by its id, in /etc/agent-proxy/secrets and in /run/agent-proxy-secrets (a rotate script chowns its new file to ${AGENT_PROMPT_AGENT_PROXY_SETUP_LOGIN_ACCOUNT_OWNERSHIP_VAR_0.name} before the mv). Root:root 644: secrets.yaml, which is policy, not a secret, and the other config; never loosen the mode of a secrets.yaml this setup did not write, since it may hold inline: values. Hooks: root-owned 755. A log folder, if the proxy logs to a file: owned by ${AGENT_PROMPT_AGENT_PROXY_SETUP_LOGIN_ACCOUNT_OWNERSHIP_VAR_0.name} at 700. The network environment file: ${AGENT_PROMPT_AGENT_PROXY_SETUP_LOGIN_ACCOUNT_OWNERSHIP_VAR_1}.
