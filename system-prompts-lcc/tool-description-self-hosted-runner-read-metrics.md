<!--
name: 'Tool Description: Self-hosted runner read metrics'
description: >-
  Description and prompt for the self_hosted_runner_read_metrics tool, telling
  the model it parses the runner's Prometheus gauges; sent with the
  self-hosted-runner toolset.
ccVersion: 2.1.224
-->
GET http://127.0.0.1:{health_port}/metrics on the local runner and parse the `claude_code_self_hosted_runner_*` Prometheus gauges into {capacity, active_sessions, last_poll_age_seconds, locked_account_email?}.
