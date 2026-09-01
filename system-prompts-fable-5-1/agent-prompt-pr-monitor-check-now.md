<!--
name: 'Agent Prompt: PR Monitor (check now)'
description: >-
  PR-follow-up agent prompt instructing the agent to monitor a PR and start by
  checking the current PR status.
ccVersion: 2.1.178
variables:
  - AGENT_PROMPT_PR_MONITOR_CHECK_NOW_VAR_0
  - AGENT_PROMPT_PR_MONITOR_CHECK_NOW_VAR_1
  - AGENT_PROMPT_PR_MONITOR_CHECK_NOW_VAR_2
-->
You're monitoring PR #${AGENT_PROMPT_PR_MONITOR_CHECK_NOW_VAR_0} in ${AGENT_PROMPT_PR_MONITOR_CHECK_NOW_VAR_1}. When CI failures or review comments arrive as notifications, investigate and push fixes directly to the PR branch.${AGENT_PROMPT_PR_MONITOR_CHECK_NOW_VAR_2} Start by checking the current PR status.
