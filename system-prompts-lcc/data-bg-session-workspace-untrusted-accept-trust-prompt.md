<!--
name: 'Data: Background Session Blocked — Accept Trust Prompt First'
description: >-
  Refusal returned when a background or forked session's workspace is untrusted,
  telling the reader to run claude there once and accept the trust prompt. It
  reaches the model through the /fork command result.
ccVersion: 2.1.281
variables:
  - DATA_BG_SESSION_WORKSPACE_UNTRUSTED_ACCEPT_TRUST_PROMPT_VAR_0
-->
Workspace not trusted. Run \`claude\` in ${DATA_BG_SESSION_WORKSPACE_UNTRUSTED_ACCEPT_TRUST_PROMPT_VAR_0} once and accept the trust prompt, then retry.
