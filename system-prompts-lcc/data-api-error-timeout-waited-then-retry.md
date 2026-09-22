<!--
name: 'Data: API Timeout Waited Then Retry'
description: >-
  Duration clause in the first-byte timeout API-error assistant message when the
  request waited through the first window and then a retry window.
ccVersion: 2.1.261
variables:
  - DATA_API_ERROR_TIMEOUT_WAITED_THEN_RETRY_VAR_0
  - DATA_API_ERROR_TIMEOUT_WAITED_THEN_RETRY_VAR_1
  - DATA_API_ERROR_TIMEOUT_WAITED_THEN_RETRY_VAR_2
-->
waited ${DATA_API_ERROR_TIMEOUT_WAITED_THEN_RETRY_VAR_0(DATA_API_ERROR_TIMEOUT_WAITED_THEN_RETRY_VAR_1)}, then ${DATA_API_ERROR_TIMEOUT_WAITED_THEN_RETRY_VAR_0(DATA_API_ERROR_TIMEOUT_WAITED_THEN_RETRY_VAR_2)} on the retry
