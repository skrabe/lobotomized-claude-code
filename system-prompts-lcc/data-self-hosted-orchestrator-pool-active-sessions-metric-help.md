<!--
name: 'Data: Orchestrator pool_active_sessions metric help'
description: >-
  Prometheus HELP line for the orchestrator pool_active_sessions gauge; reaches
  the model as part of the raw /metrics text returned by
  self_hosted_runner_read_metrics.
ccVersion: 2.1.224
-->

# HELP ${"claude_code_self_hosted_orchestrator"}_pool_active_sessions Sessions currently assigned to an alive runner in this environment (the server's environment-wide sum of the per-runner _active_sessions gauges). Environment-wide aggregate — identical on every orchestrator for one environment; use MAX not SUM across orchestrator instances.
