<!--
name: 'Data: Orchestrator spawn_hooks_total metric help'
description: >-
  Prometheus HELP line for the orchestrator spawn_hooks_total counter, including
  its exit-code contract; reaches the model via the read_metrics raw payload.
ccVersion: 2.1.224
-->
# HELP ${"claude_code_self_hosted_orchestrator"}_spawn_hooks_total spawn-runner hook outcomes since process start (exit-code contract: ok=0, retryable=1/timeout/signal, non_retryable=>=2/ENOENT/EACCES). Counts orchestrator hook invocations (seat + warm), NOT runner child spawns — NOT comparable to the runner's sessions_started_total (capacity>1, warm environments, and per-runner re-spawns all diverge them).
