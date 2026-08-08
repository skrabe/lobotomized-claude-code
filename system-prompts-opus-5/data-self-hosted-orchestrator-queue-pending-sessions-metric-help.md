<!--
name: 'Data: Orchestrator queue_pending_sessions metric help'
description: >-
  Prometheus HELP line for the claimable spawn-hint queue gauge; reaches the
  model via the read_metrics raw payload.
ccVersion: 2.1.224
-->
# HELP claude_code_self_hosted_orchestrator_queue_pending_sessions Spawn-hint queue rows claimable right now (eta < now, unclaimed, not circuit-broken). Server-side aggregate for this environment.
