<!--
name: 'Data: Orchestrator pool_pending_sessions metric help'
description: >-
  Prometheus HELP line for the environment-wide pending-session gauge used for
  autoscaling; reaches the model via the read_metrics raw payload.
ccVersion: 2.1.224
-->
# HELP claude_code_self_hosted_orchestrator_pool_pending_sessions Total sessions currently waiting on a runner for this environment (the UI "N ahead of you" number). Autoscale on this, not on queue_pending_sessions.
