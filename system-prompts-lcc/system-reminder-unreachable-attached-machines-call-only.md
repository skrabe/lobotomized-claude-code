<!--
name: 'System Reminder: Unreachable attached machines (call only)'
description: >-
  Explains that a call to an unreachable machine takes up to 10 seconds to fail
  and is the only way to learn it is back, so it should be made only when the
  user says so
ccVersion: 2.1.295
variables:
  - UNREACHABLE_MACHINES_NOTICE
  - IS_SINGLE_OFFLINE_MACHINE
  - CALL_BASED_RETRY_GUIDANCE
-->
${UNREACHABLE_MACHINES_NOTICE} A call to ${IS_SINGLE_OFFLINE_MACHINE?"it":"one of them"} takes up to 10 seconds to fail and ${CALL_BASED_RETRY_GUIDANCE}
