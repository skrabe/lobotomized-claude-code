<!--
name: 'Data: API error status fallback'
description: API error text naming only the status when the error has no message
ccVersion: 2.1.316
variables:
  - DATA_API_ERROR_STATUS_FALLBACK_VAR_0
-->
API error (status ${DATA_API_ERROR_STATUS_FALLBACK_VAR_0.status??"unknown"})
