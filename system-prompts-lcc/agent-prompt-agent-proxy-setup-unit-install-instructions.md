<!--
name: 'Agent prompt: agent proxy setup unit install instructions'
description: >-
  Describes the systemd unit to install, allowed added lines, AWS profile
  placement, TimeoutStopSec and the reload/enable commands
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_0
  - AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_1
  - AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_2
  - AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_3
  - AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_4
-->
Unit: a ${AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_0} unit, at ${AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_1}${AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_0==="system"?", which needs root to write":""}. Install this text as given, adding only the SELF_HOSTED_AGENT_PROXY_* settings, the hook and secrets lines, and the identity lines the skill's steps call for: AWS_CONFIG_FILE, AWS_SHARED_CREDENTIALS_FILE, AWS_REGION, AWS_EC2_METADATA_SERVICE_ENDPOINT, GOOGLE_APPLICATION_CREDENTIALS, and, in a user unit only, its UnsetEnvironment= line, which never names a variable the admin sets on purpose. A profile the proxy needs goes under [default], in a root:root 644 file with no keys in it, which AWS_CONFIG_FILE names. Its TimeoutStopSec is the hook timeout plus 15 seconds when the proxy runs hooks (their timeout defaults to ${AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_2}s), else 30; set it so if you add hooks or a hook timeout. ${AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_0==="system"?"Then the user runs":"Then run"} \`${AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_3} daemon-reload\` and \`${AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_3} enable --now ${AGENT_PROMPT_AGENT_PROXY_SETUP_UNIT_INSTALL_INSTRUCTIONS_VAR_4}\`.
