<!--
name: 'Tool parameter: Cowork staging retryable flag'
description: >-
  Model-facing describe() text for the staging.retryable field in the Cowork
  staged-call result schema.
ccVersion: 2.1.206
-->
Present when the failure class is known (lane transport verdict, CAS rejection): true = safe to re-drive with the same request_id, false = deterministic. Absent = unknown; treat as non-retryable and switch on error_code.
