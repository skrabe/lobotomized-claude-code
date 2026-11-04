<!--
name: 'Data: Orchestrator session_queue_wait_seconds metric help'
description: >-
  Prometheus HELP line for the session queue-wait histogram; reaches the model
  via the read_metrics raw payload.
ccVersion: 2.1.224
-->

# HELP claude_code_self_hosted_orchestrator_session_queue_wait_seconds Seconds each session waited in the queue before the orchestrator claimed it for spawn (HTTP Date header - SpawnHint.queue_wait_started_at; seat hints only). For p50/p99 queue-time SLOs and "queue wait > N" alerting.
