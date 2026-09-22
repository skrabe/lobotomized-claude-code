<!--
name: 'Data: Runner poll_errors_total metric help'
description: >-
  Prometheus HELP line for the runner PollWork error-kind counter; reaches the
  model via the read_metrics raw payload.
ccVersion: 2.1.224
variables:
  - DATA_SELF_HOSTED_RUNNER_POLL_ERRORS_METRIC_HELP_VAR_0
-->
# HELP ${DATA_SELF_HOSTED_RUNNER_POLL_ERRORS_METRIC_HELP_VAR_0}_poll_errors_total PollWork request failures by error kind (transport=no HTTP response; timeout=client deadline; 5xx/429/4xx by status). All five series present from process start so rate() works and absent() means process-down.
