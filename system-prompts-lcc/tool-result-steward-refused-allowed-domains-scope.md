<!--
name: 'Tool Result: Steward allowed_domains scope'
description: >-
  Steward hook refusal when allowed_domains is used beyond the watch's own git
  fetch/push to its host
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_STEWARD_REFUSED_ALLOWED_DOMAINS_SCOPE_VAR_0
-->
allowed_domains may stand only on this watch's own git fetch or git push, alone on its call, and may name only ${TOOL_RESULT_STEWARD_REFUSED_ALLOWED_DOMAINS_SCOPE_VAR_0}
