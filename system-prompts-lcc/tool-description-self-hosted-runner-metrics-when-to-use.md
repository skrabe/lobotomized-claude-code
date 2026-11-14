<!--
name: 'Tool Description: self-hosted runner metrics when to use'
description: whenToUse for the tool that reads a local self-hosted runner's /metrics gauges
ccVersion: 2.1.325
variables:
  - TOOL_DESCRIPTION_SELF_HOSTED_RUNNER_METRICS_WHEN_TO_USE_VAR_0
  - TOOL_DESCRIPTION_SELF_HOSTED_RUNNER_METRICS_WHEN_TO_USE_VAR_1
-->
When you are about to report a local self-hosted runner's capacity, active sessions, time since last poll or locked account, use it and not curl on /metrics; for whether the runner is up use ${TOOL_DESCRIPTION_SELF_HOSTED_RUNNER_METRICS_WHEN_TO_USE_VAR_0}, for environment-wide totals ${TOOL_DESCRIPTION_SELF_HOSTED_RUNNER_METRICS_WHEN_TO_USE_VAR_1}.
