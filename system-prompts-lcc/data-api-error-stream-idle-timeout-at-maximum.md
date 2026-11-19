<!--
name: 'Data: API error stream idle timeout at maximum'
description: >-
  Stream-idle API-error text when CLAUDE_STREAM_IDLE_TIMEOUT_MS is already at
  its maximum, pointing to API_FORCE_IDLE_TIMEOUT=0
ccVersion: 2.1.328
variables:
  - DATA_API_ERROR_STREAM_IDLE_TIMEOUT_AT_MAXIMUM_VAR_0
-->
${DATA_API_ERROR_STREAM_IDLE_TIMEOUT_AT_MAXIMUM_VAR_0} That is the longest CLAUDE_STREAM_IDLE_TIMEOUT_MS allows, and API_FORCE_IDLE_TIMEOUT=0 removes this limit.
