<!--
name: 'Tool Description: Self-hosted runner tail log'
description: >-
  Description and prompt for the self_hosted_runner_tail_log tool, telling the
  model the runner log is secret-redacted before it reaches model context; sent
  with the self-hosted-runner toolset.
ccVersion: 2.1.224
-->
Read the last N bytes of the runner's --log-file with the shared secret redaction (key=value secrets, sk-ant/Bearer/Basic, URL userinfo, JWTs, and VCS/service PATs — see redact() in src/utils/secretRedaction.ts for the current rule set) applied before the content reaches model context.
