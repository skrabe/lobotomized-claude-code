<!--
name: Allowed Domains Classifier Review Reason
description: >-
  decisionReason for the allowed_domains classifier-review ask; on decline the
  model reads it as the tool_result.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_ALLOWED_DOMAINS_CLASSIFIER_REVIEW_REASON_VAR_0
-->
A ${TOOL_RESULT_ALLOWED_DOMAINS_CLASSIFIER_REVIEW_REASON_VAR_0.name} call that carries allowed_domains is reviewed by the auto-mode classifier; allow rules and hook allows approve the command, not the hosts.
