<!--
name: 'Agent prompt: agent proxy setup ExecStart pinned proxy'
description: >-
  Explains the unit ExecStart runs the pinned, already-downloaded proxy, forbids
  placing the binary, and the no-restart exit status
ccVersion: 2.1.332
variables:
  - AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_0
  - AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_1
  - AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_2
  - AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_3
-->
Its ExecStart runs the proxy: \`${AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_0} run\` starts agent proxy ${AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_1.version}, which this Claude Code pins, from ${AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_2}, where it is already downloaded and checked against this Claude Code's hash for it. Do not download, copy or place the proxy binary. \`run\` exits ${AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_3} on a refusal no restart fixes, which RestartPreventExitStatus=${AGENT_PROMPT_AGENT_PROXY_SETUP_EXECSTART_RUNS_PINNED_PROXY_VAR_3} stops restarting.
