<!--
name: 'Data: Orchestrator poll_errors_total metric help'
description: >-
  Prometheus HELP line for the orchestrator PollSpawnHints error-kind counter;
  reaches the model via the read_metrics raw payload.
ccVersion: 2.1.224
-->
# HELP claude_code_self_hosted_orchestrator_poll_errors_total PollSpawnHints request failures by error kind (transport=no HTTP response; timeout=client deadline; 5xx/429/4xx by status). All five series present from process start so rate() works and absent() means process-down.
