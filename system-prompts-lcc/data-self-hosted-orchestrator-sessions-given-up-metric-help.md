<!--
name: 'Data: Self-hosted orchestrator sessions given up metric help'
description: >-
  Prometheus HELP text for the orchestrator counter of sessions Anthropic gave
  up starting a runner for, by reason
ccVersion: 2.1.328
-->
# HELP claude_code_self_hosted_orchestrator_sessions_given_up_total Times since process start that Anthropic gave up starting a runner for a session, as its answers to this orchestrator said. lease_expiry: at least ten tries in a row gave no runner, the last because none registered in time. retries_exhausted: at least ten in a row gave none, the last by a retryable failure that this orchestrator reported. Tries that never reached an orchestrator count among the ten. hook_declined: this orchestrator reported a non-retryable failure (the hook exited 2 or more, could not be executed, or was not run because a session label has a value that --hook-label does not allow). Each give-up is counted by at most one instance; SUM across instances.
