<!--
name: 'Tool Result: Cloud Session Local Changes Bundle Failed'
description: >-
  Cloud-session create-fail message when working-tree upload fails without a
  detail string, including the unsupported_layout recovery.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_BUNDLE_FAILED_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_BUNDLE_FAILED_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_BUNDLE_FAILED_VAR_2
  - TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_BUNDLE_FAILED_VAR_3
-->
No cloud session was started: ${TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_BUNDLE_FAILED_VAR_0[t]}, and the working tree could not be uploaded instead (${TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_BUNDLE_FAILED_VAR_1[e.why]}). ${TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_BUNDLE_FAILED_VAR_2.why==="unsupported_layout"?"Start the session from the repository's main checkout":"Try again"}; or, to start from GitHub, ${TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_BUNDLE_FAILED_VAR_3}
